// src/Header.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Header.css'; // Create this CSS file for styling

const Header = () => {
    return (
        <header className="header">
            <div className="logo">VUTEQ</div>
            <nav className="nav">
                <Link to="/">Home</Link>
                <Link to="/about">About</Link>
                <Link to="/contact">Contact</Link>
                <Link to="/ext">Extentions</Link>
            </nav>
        </header>
    );
};

export default Header;