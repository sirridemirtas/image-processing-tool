import { useContext, useState } from "react";
import { AppContext } from "../store";

export default function DownloadButton() {
  const { state } = useContext(AppContext);
  const [loading, setLoading] = useState(false);

  return (
    <button
      className={
        loading ? "download-button download-button--loading" : "download-button"
      }
      onClick={() => {
        setLoading(true);

        fetch(`http://localhost:5000/download?filename=${state.image}`)
          .then((response) => {
            setLoading(false);
            return response.blob();
          })
          .then((blob) => {
            const url = window.URL.createObjectURL(new Blob([blob]));
            const link = document.createElement("a");
            link.href = url;
            link.setAttribute("download", state.image);
            document.body.appendChild(link);
            link.click();
            setLoading(false);
          });
      }}
    >
      {loading ? "Downloading..." : "Download"}
    </button>
  );
}
