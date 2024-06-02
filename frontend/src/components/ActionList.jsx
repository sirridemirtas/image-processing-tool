import { useContext } from "react";
import { AppContext } from "../store";

export default function ActionList() {
  const { state, dispatch } = useContext(AppContext);

  const handleDeleteAction = (e, index) => {
    e.preventDefault();
    dispatch({
      type: "DELETE_ACTION",
      payload: index,
    });
  };

  const handleMoveUp = (e, index) => {
    e.preventDefault();
    dispatch({
      type: "MOVE_UP",
      payload: index,
    });
  };

  const handleMoveDown = (e, index) => {
    e.preventDefault();
    dispatch({
      type: "MOVE_DOWN",
      payload: index,
    });
  };

  return (
    <div className="action_list">
      <h1>Actions</h1>
      <table>
        <thead>
          <tr>
            <th>Action Type</th>
            <th>Value</th>
          </tr>
        </thead>
        <tbody>
          {state.actions.map((action, index) => (
            <tr key={index}>
              <td>{action.type}</td>
              <td>{action.value}</td>
              <td>
                <button onClick={(e) => handleDeleteAction(e, index)}>
                  Delete
                </button>
              </td>
              <td>
                <button onClick={(e) => handleMoveUp(e, index)}>Up</button>
              </td>
              <td>
                <button onClick={(e) => handleMoveDown(e, index)}>Down</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
