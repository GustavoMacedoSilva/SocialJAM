import { useSearchParams } from "react-router-dom";
/**
 * Os parâmetros "name" e "album" são extraídos da query string da URL e exibidos na página.
 *
 *  Um container mostrando os valores dos parâmetros "name" e "album".
x */

function TasksPage() {
  const [searchParams] = useSearchParams();
  const name = searchParams.get("name");
  const album = searchParams.get("album");


  return (
  <div className="h-screen w-screen bg-slate-950 p-6 justify-center flex">

    <div className="w-[500px] space-y-4">
      
      <h1 className="text-3xl text-slate-100 font-bold text-center">
        Detalhes da Banda
      </h1>

      <div className="bg-slate-400 p-4 rounded-md"> 
        <h2 className="text-xl font-bold text-white">
          {name}
        </h2>
        <p className="text-xl font-bold text-white">
          {album}
        </p>
        
      </div>
    </div>

  </div>
  );

}

export default TasksPage;
