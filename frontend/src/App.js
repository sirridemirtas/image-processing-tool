import { useEffect, useContext } from "react";
import { AppContext } from "./store";

import Editor from "./components/Editor";
import UploadImage from "./components/UploadImage";

import "./App.css";

function App() {
  const { state } = useContext(AppContext);

  useEffect(() => {
    localStorage.setItem("editor_state", JSON.stringify(state));
  }, [state]);

  return (
    <div className="app">{state?.image ? <Editor /> : <UploadImage />}</div>
  );
}

export default App;
