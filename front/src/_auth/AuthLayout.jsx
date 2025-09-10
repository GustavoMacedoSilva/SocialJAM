import {Outlet, Navigate} from "react-router-dom"

const AuthLayout = () => {
  const isAuthenticated = false; // Lógica para verificar se o usuário está autenticado
  return (
    <>
      {isAuthenticated ? (
          <Navigate to="/" />
        ):(
          <>
            <section className="flex flex-1 justify-center items-center flex-col py-10">
              <Outlet />
            </section>
            <img
              src="/assets/images/Katador.jpg"
              alt="logo"
              className="hidden md:block w-1/2 object-cover bg-no-repeat"
            />

          </>
        )
      }  
    </>
  )
}

export default AuthLayout