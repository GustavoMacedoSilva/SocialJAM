import { ChevronRightIcon, TrashIcon } from "lucide-react";
import { useNavigate } from "react-router-dom";


function Tasks({ tasks, onTaskClick, onTaskDelete }) {

  const navigate = useNavigate();

  function onSeeDetailsClick(task) {

    const queryParams = new URLSearchParams();
    queryParams.set("name", task.name);
    queryParams.set("album", task.album);
    navigate(`/tasks?${queryParams.toString()}`);
  }

  
  return (
    <ul className="space-y-4 p-6 bg-slate-400 rounded-md shadow">
      {tasks.map((task) => (
        <li key={task.id} className="flex gap-2">
          <button
            onClick={() => onTaskClick(task.id)}
            className={`bg-slate-600 w-full text-white rounded-md p-2 ${
              task.reminder && "line-through"
            }`}
          >
            {task.name}
          </button>

          <button onClick={() => onSeeDetailsClick(task)} className="bg-slate-600 p-2 rounded-md text-white">
            <ChevronRightIcon />
          </button>

          <button
            onClick={() => onTaskDelete(task.id)}
            className="bg-slate-600 p-2 rounded-md text-white"
          >
            <TrashIcon />
          </button>
        </li>
      ))}
    </ul>
  );
}

export default Tasks;
