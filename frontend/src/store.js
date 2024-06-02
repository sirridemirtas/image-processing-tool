import { createContext, useReducer } from "react";

const initialState = localStorage.getItem("state")
  ? JSON.parse(localStorage.getItem("editor_state"))
  : {
      image: "sample.jpg",
      actions: [
        /* {
            order: 1,
            type: "rotate",
            value: 45
        },
        {
            order: 2,
            type: "brightness",
            value: 50
        },
        {
            order: 3,
            type: "contrast",
            value: 75
        }, */
      ],
    };

const reducer = (state, action) => {
  switch (action.type) {
    case "SET_IMAGE_URL":
      return { ...state, image: action.payload };
    case "ADD_ACTION":
      return { ...state, actions: [...state.actions, action.payload] };
    case "REMOVE_ACTION":
      return {
        ...state,
        actions: state.actions.filter(
          (action) => action.order !== action.payload
        ),
      };
    case "UPDATE_ACTION":
      return {
        ...state,
        actions: state.actions.map((action) =>
          action.order === action.payload.order ? action.payload : action
        ),
      };
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
