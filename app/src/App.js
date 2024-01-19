import './App.css';
import Geolocation from './pages/geolocation.js';
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

function App() {
  return (
    <Router>
      <div className='App'>
        <main>
          <Routes>
            <Route path='/' element={<Geolocation />} /> {/* Use Geolocation with uppercase 'G' */}
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
