import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.extension import db
from app import create_app

app = create_app("DevelopmentConfig")
with app.app_context():
    db.create_all()
    

if __name__ == '__main__':
    app.run(debug=True)
