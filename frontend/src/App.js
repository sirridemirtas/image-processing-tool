import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [data, setdata] = useState({
    message: "",
  });

  useEffect(() => {
    fetch("/hello").then((res) =>
      res.json().then((data) => {
        setdata({
          message: data.message,
        });
      })
    );
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>React and flask</h1>
        <p>{data.message}</p>
      </header>
    </div>
  );
}

export default App;
