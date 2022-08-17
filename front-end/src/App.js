import logo from './adamLogo.png';
import './App.css';
import userInput from './UserInput';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <form>
          <label>
            Name:
            <input type="text" name="name" />
            </label>
            <input type="submit" value="Submit" />
        </form>
        <a
          className="App-link"
          href="https://www.instagram.com/binary.dreams/"
          target="_blank"
          rel="noopener noreferrer"
        >
          Insta
        </a>
      </header>
    </div>
  );
}

export default App;
