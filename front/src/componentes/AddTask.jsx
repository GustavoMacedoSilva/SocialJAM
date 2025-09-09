import { useState } from "react";

function AddTask({ onAddTaskSubmit }) {
  const [name, setName] = useState("");
  const [album, setAlbum] = useState("");

  return (
    <div className="space-y-4 p-6 bg-slate-400 rounded-md shadow flex flex-col">
      <input
        type="text"
        placeholder="Nome da Banda"
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
        value={name}
        onChange={(event) => setName(event.target.value)}
      />

      <input
        type="text"
        placeholder="Nome do Album"
        className="border border-slate-300 outline-slate-400 px-4 py-2 rounded-md"
        value={album}
        onChange={(event) => setAlbum(event.target.value)}
      />

      <button
        onClick={() => {

          if (!name.trim() || !album.trim()) {
            alert("Por favor, preencha todos os campos.");
            return;
          }
          onAddTaskSubmit(name, album);
          setName("");
          setAlbum("");
        }}
        className="bg-slate-600 text-white rounded-md p-2 hover:bg-slate-700 transition"
      >
        Adicionar Banda
      </button>
    </div>
  );
}

export default AddTask;
