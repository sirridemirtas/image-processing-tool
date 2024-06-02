import { useContext } from "react";
import { AppContext } from "../store";

export default function ResetButton() {
  const { dispatch } = useContext(AppContext);

  return (
    <button
      className={"reset-button"}
      onClick={() => {
        dispatch({
          type: "RESET",
        });
      }}
    >
      Reset App
    </button>
  );
}
