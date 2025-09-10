import {Routes, Route} from "react-router-dom"

import './globals.css';
import SigninForms from "./_auth/forms/SigninForms";
import {Home} from "./_root/pages";
import SignupForms from "./_auth/forms/SignupForms";
import AuthLayout from "./_auth/AuthLayout";
import RootLayout from "./_root/RootLayout";



const App = () => {
  return (
    <main className="flex h-screen">
      <Routes>
        {/* Rotas públicas */}
        <Route element={<AuthLayout />}>
          <Route path="/signup" element={<SignupForms />} />
          <Route path="/signin" element={<SigninForms />} />
        </Route>

        {/* Rotas privadas */}
        <Route element={<RootLayout />}>
          <Route index element={<Home />} />
        </Route>

      </Routes>
    </main>
  )
}

export default App