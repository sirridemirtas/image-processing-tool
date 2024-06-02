import { createContext, useReducer } from "react";

const initialState = localStorage.getItem("editor_state")
  ? JSON.parse(localStorage.getItem("editor_state"))
  : {
      // uploaded image name or any image name from ../backend/static/images/raw folder
      image: "", // for example: sample.jpg

      actions: [
        /* {
          type: "rotate",
          value: 45,
        },
        {
          type: "brightness",
          value: 50,
        },
        {
          type: "contrast",
          value: 75,
        }, */
      ],
    };

const reducer = (state, action) => {
  const payload = action.payload;

  switch (action.type) {
    case "SET_IMAGE_URL":
      return { ...state, image: payload };

    case "ADD_ACTION":
      return {
        ...state,
        actions: [...state.actions, payload],
      };

    case "DELETE_ACTION":
      // delete action by index
      return {
        ...state,
        actions: state.actions.filter((action, index) => index !== payload),
      };

    case "UPDATE_ACTION":
      // update action by index
      return {
        ...state,
        actions: state.actions.map((action, index) =>
          index === payload.index ? payload.action : action
        ),
      };

    case "MOVE_UP":
      const upIndex = payload; // payload doğrudan index değeri

      if (upIndex > 0) {
        const upActions = [...state.actions];
        const upAction = upActions[upIndex];
        upActions.splice(upIndex, 1);
        upActions.splice(upIndex - 1, 0, upAction);
        return { ...state, actions: upActions };
      }
      return state;

    case "MOVE_DOWN":
      const downIndex = payload;

      if (downIndex < state.actions.length - 1) {
        const downActions = [...state.actions];
        const downAction = downActions[downIndex];
        downActions.splice(downIndex, 1);
        downActions.splice(downIndex + 1, 0, downAction);
        return { ...state, actions: downActions };
      }
      return state;

    case "CLEAR_ACTIONS":
      return { ...state, actions: [] };

    case "RESET":
      return { image: "", actions: [] };

    default:
      return state;
  }
};

export const AppContext = createContext();

export const AppProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <AppContext.Provider value={{ state, dispatch }}>
      {children}
    </AppContext.Provider>
  );
};
