import { useContext, useRef } from "react";
import { AppContext } from "../store";

export default function UploadImage() {
  const { dispatch } = useContext(AppContext);
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
