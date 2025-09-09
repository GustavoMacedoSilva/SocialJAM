import { useState } from "react";
import AddTask from "./componentes/AddTask";
import Tasks from "./componentes/Tasks";
import {v4} from "uuid";

function App() {
  // State (estado) - variáveis que eu quero que, quando mudarem, atualizem a interface
  // message = valor do state // setMessage = função para atualizar o valor do state
  const [tasks, setTask] = useState([
    { id: v4(), name: "Legião Urbana", album: "As Quatro Estações", reminder: true },
    { id: v4(), name: "Titãs", album: "Cabeça Dinossauro", reminder: false },
    { id: v4(), name: "Paralamas do Sucesso", album: "O Passo do Lui", reminder: true },

  ]);

  function onTaskClick(taskId) {
    const newTasks = tasks.map((task) => {
      // preciso atualizar essa tarefa
      if (task.id === taskId) {
        return { ...task, reminder: !task.reminder };
      }

      return task; // não preciso atualizar essa tarefa
    });

    setTask(newTasks);
  }

  function onTaskDelete(taskId) {
    const newTasks = tasks.filter((task) => task.id !== taskId);
    setTask(newTasks);
  }

  function onAddTaskSubmit(name, album) {
    const newTask = {
      id: v4(),
      name: `${name} - ${album}`,
      album: album,
      reminder: false,
    };
    setTask([...tasks, newTask]);
  }

  return (
    <div className="w-screen h-screen bg-slate-950 flex justify-center p-6">
      <div className="w-[500px] space-y-4">
        <h1 className="text-3xl text-slate-50 font-bold text-center">
          Gerenciador de Albuns
        </h1>

        <AddTask onAddTaskSubmit={onAddTaskSubmit} />

        <Tasks
          tasks={tasks}
          onTaskClick={onTaskClick}
          onTaskDelete={onTaskDelete}
        />
      </div>
    </div>
  );
}

export default App;
