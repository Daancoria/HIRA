import React from 'react';
import background from '../assets/background.png';

const MockDesktop: React.FC = () => {
  return (
    <div
      style={{
        width: '100vw',
        height: '100vh',
        backgroundImage: `url(${background})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat',
        position: 'relative',
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: '50%',
          left: '50%',
          transform: 'translate(-50%, -50%)',
          textAlign: 'center',
          color: '#fff',
          fontSize: '24px',
        }}
      >
        Welcome To Vikara Health Solutions!
      </div>
    </div>
  );
};

export default MockDesktop;
