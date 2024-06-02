import { useContext, useRef, useState } from "react";
import { AppContext } from "../store";

export default function AddAction() {
  const { dispatch } = useContext(AppContext);
  const selectAddAction = useRef();

  const actionValue = useRef();

  const [selectedAction, setSelectedAction] = useState("");

  const handleAddAction = (e) => {
    e.preventDefault();
    if (!selectedAction || !actionValue.current.value) {
      return;
    }
    dispatch({
      type: "ADD_ACTION",
      payload: {
        //order: state.actions ? state.actions.length + 1 : 1,
        type: selectedAction,
        value: actionValue.current.value,
      },
    });
    selectAddAction.current.value = "";
    setSelectedAction("");
    actionValue.current.value = "";
  };

  return (
    <div className="add_actions">
      <h1>Add Actions</h1>
      <select
        ref={selectAddAction}
        className="select-action"
        onChange={(e) => setSelectedAction(e.target.value)}
      >
        <option value="">Select an action</option>
        <option value="brightness">Brightness</option>
        <option value="contrast">Contrast</option>
        <option value="flip">Flip</option>
        <option value="gaussian_blur">Gaussian Blur</option>
        <option value="grayscale">Grayscale</option>
        <option value="rgb_order">RGB Order</option>
        <option value="rotate">Rotate</option>
      </select>

      <form onSubmit={handleAddAction}>
        {selectedAction === "brightness" ? (
          <div>
            <input
              ref={actionValue}
              type="number"
              min="0"
              max="100"
              step="1"
              defaultValue="50"
            />
          </div>
        ) : selectedAction === "contrast" ? (
          <div>
            <input
              ref={actionValue}
              type="number"
              min="0"
              max="100"
              step="1"
              defaultValue="75"
            />
          </div>
        ) : selectedAction === "flip" ? (
          <div>
            <select ref={actionValue}>
              <option value="">Select Axis</option>
              <option value="h">Horizontal</option>
              <option value="v">Vertical</option>
              <option value="b">Both</option>
            </select>
          </div>
        ) : selectedAction === "gaussian_blur" ? (
          <div>
            <input
              ref={actionValue}
              type="number"
              min="1"
              max="100"
              step="2"
              defaultValue="1"
            />
          </div>
        ) : selectedAction === "grayscale" ? (
          <div>
            <select ref={actionValue}>
              <option value="">Select Band</option>
              <option value="r">Red</option>
              <option value="g">Green</option>
              <option value="b">Blue</option>
            </select>
          </div>
        ) : selectedAction === "rgb_order" ? (
          <div>
            <select ref={actionValue}>
              <option value="bgr">BGR</option>
              <option value="brg">BRG</option>
              <option value="gbr">GBR</option>
              <option value="grb">GRB</option>
              <option value="rgb">RGB</option>
              <option value="rbg">RBG</option>
            </select>
          </div>
        ) : selectedAction === "rotate" ? (
          <div>
            <input
              ref={actionValue}
              type="range"
              min="0"
              max="360"
              step="1"
              defaultValue="0"
            />
          </div>
        ) : null}
        <button type="submit">Add Action</button>
      </form>
    </div>
  );
}
