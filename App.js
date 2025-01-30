// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css'; // Global styles
import Header from './Header';
import Footer from './Footer';
import Home from './Home';
import About from './About';
import Contact from './Contact';

function App() {
    return (
        <Router>
            <div>
                <Header />
                    <Routes>
                        <Route path="/" element={<Home />} />{/**/}
                        <Route path="/about" element={<About />} />
                        <Route path="/contact" element={<Contact />} />
                    </Routes>
                <Footer />
            </div>
        </Router>
    );
}

export default App;