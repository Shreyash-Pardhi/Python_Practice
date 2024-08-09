import React from 'react';
import './Popup.css'; // Create your own CSS for modal styles

const Popup = ({ show, onClose, content }) => {
  if (!show) return null;

  return (
    <div className='modal-overlay'>
      <div className='modal-content'>
        <button className='close-btn' onClick={onClose}>X</button>
        <div>{content}</div>
      </div>
    </div>
  );
};

export default Popup;