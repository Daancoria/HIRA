import logging

from datetime import datetime, timedelta, timezone
from jose import jwt
import jose
from functools import wraps
from flask import request, jsonify, g

logger = logging.getLogger(__name__)
logger.setLevel(logging.WARNING) 

SECRET_KEY = "abc123"

def encode_token(user_id): #using unique pieces of info to make our tokens user specific
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(days=0,hours=1), #Setting the expiration time to an hour past now
        'iat': datetime.now(timezone.utc), #Issued at
        'sub':  str(user_id) #This needs to be a string or the token will be malformed and won't be able to be decoded.
    }

    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
    
        if 'Authorization' in request.headers:
            
            token = request.headers['Authorization'].split()[1]

            if not token:
                logger.warning("Security incident: Missing token in Authorization header")
                return jsonify({'message': 'missing token'}), 400
            
            try:        
            
                data = jwt.decode(token, SECRET_KEY, algorithms='HS256')
                print(data)
                user_id = data['sub']
                user = user.query.get(user_id)

                if not user:
                    logger.warning(f"Not found: User does not exist. Error: {str(e)}")
                    return jsonify({'message': 'User not found'}), 404
                
                g.current_user = user

            except jwt.ExpiredSignatureError as e:
                logger.warning(f"Security incident: Expired token used. Error: {str(e)}")
                return jsonify({'message':'token expired'}), 400
            
            except jwt.InvalidTokenError:
                logger.warning(f"Security incident: Invalid token used. Error: {str(e)}")
                return jsonify({'message': 'invalid token'}), 400
            
            return f(*args, **kwargs)
        else:
            logger.warning("Security incident: No Authorization header provided")
            return jsonify({'message': 'You must be logged in to access this.'}), 400

    return decorated