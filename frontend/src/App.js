import React, { useState, useEffect, useContext, useRef } from "react";
import { AppContext } from "./store";
import "./App.css";

function UploadImage() {
  const { state, dispatch } = useContext(AppContext);
  const fileInput = useRef(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!fileInput.current.files.length) {
      return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.current.files[0]);

    fetch("http://localhost:5000/upload", {
      method: "POST",
      body: formData,
    })
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        const { filename } = data;
        dispatch({ type: "SET_IMAGE_URL", payload: filename });
      })
      .catch((error) => {
        console.error("Error uploading file:", error);
      });
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" ref={fileInput} name="file" />
        <button type="submit">Upload</button>
      </form>
    </div>
  );
}

function Editor() {
  const { state, dispatch } = useContext(AppContext);

  useEffect(() => {
    console.log(state);
  }, []);

  return (
    <div>
      {state.image && (
        <img src={`http://localhost:5000/process?filename=${state.image}`} />
      )}
    </div>
  );
}

function App() {
  /* useEffect(() => {
    fetch("/hello").then((res) =>
      res.json().then((data) => {
        setdata({
          message: data.message,
        });
      })
    );
  }, []); */

  const { state, dispatch } = useContext(AppContext);

  useEffect(() => {
    console.log(state);
    localStorage.setItem("editor_state", JSON.stringify(state));
  }, [state]);

  return (
    <div className="App">{state?.image ? <Editor /> : <UploadImage />}</div>
  );
}

export default App;
