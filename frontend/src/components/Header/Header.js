import React from 'react';
import { useNavigate } from 'react-router-dom';
import './Header.css';
import logo from './Cakemania.png';

function Header() {
  const navigate = useNavigate();

  const handleNavigation = () => {
    navigate('/');
  };

  return (
    <header className="App-header" onClick={handleNavigation}>
      <img src={logo} alt="Logo" />
      <h1>Welcome to Cakemania!</h1>
    </header>
  );
}

export default Header;
