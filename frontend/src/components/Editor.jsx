import { useContext } from "react";
import { TransformWrapper, TransformComponent } from "react-zoom-pan-pinch";
import { AppContext } from "../store";

import ActionList from "./ActionList";
import AddAction from "./AddAction";
import DownloadButton from "./DownloadButton";
import ResetButton from "./ResetButton";

export default function Editor() {
  const { state } = useContext(AppContext);

  const url =
    `http://localhost:5000/process?filename=${state.image}` +
    state.actions
      .map((action) => {
        return `&${action.type}=${action.value}`;
      })
      .join("");

  return (
    <div className="image-container">
      {state.image && (
        <>
          <TransformWrapper centerOnInit={true} centerZoomedOut={true}>
            <TransformComponent>
              <img
                src={url}
                alt="Uploaded"
                style={{
                  maxWidth: "100%",
                  maxHeight: "100%",
                  display: "block",
                  margin: "auto",
                }}
              />
            </TransformComponent>
          </TransformWrapper>

          <DownloadButton />
          <div className="actions">
            <AddAction />
            <ActionList />
            <ResetButton />
          </div>
        </>
      )}
    </div>
  );
}
