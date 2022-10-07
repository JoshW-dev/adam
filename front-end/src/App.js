import logo from './adamLogo.png';
import './App.css';
import UserInput from './components/input';
import React, { Component }  from 'react';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <UserInput name = "test"/>
        
        <a
          className="App-link"
          href="https://www.instagram.com/binary.dreams/"
         
         
        >
          Insta
        </a>
      </header>
    </div>
  );
}

export default App;
