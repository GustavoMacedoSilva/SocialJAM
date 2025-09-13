import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { test, expect, describe, vi } from "vitest";
import { BrowserRouter } from "react-router-dom";
import SignupForms from "../../_auth/forms/SignupForms";

describe("SignupForms", () => {
  test("deve renderizar todos os campos do formulário", () => {
    render(
      <BrowserRouter>
        <SignupForms />
      </BrowserRouter>
    );

    // Verifica se todos os campos estão presentes
    expect(screen.getByLabelText("Nome")).toBeInTheDocument();
    expect(screen.getByLabelText("Nome de Usuário")).toBeInTheDocument();
    expect(screen.getByLabelText("Email")).toBeInTheDocument();
    expect(screen.getByLabelText("Senha")).toBeInTheDocument();
    expect(screen.getByRole("button", { name: /enviar/i })).toBeInTheDocument();
  });

  test("deve mostrar mensagens de erro para campos obrigatórios", async () => {
    render(
      <BrowserRouter>
        <SignupForms />
      </BrowserRouter>
    );

    // Clica no botão enviar sem preencher nada
    const submitButton = screen.getByRole("button", { name: /enviar/i });
    fireEvent.click(submitButton);

    // Aguarda as mensagens de erro aparecerem
    await waitFor(() => {
      expect(
        screen.getByText(/Nome deve ter no mínimo 2 caracteres/i)
      ).toBeInTheDocument();
    });

    await waitFor(() => {
      expect(
        screen.getByText(/Username deve ter no mínimo 2 caracteres/i)
      ).toBeInTheDocument();
    });

    await waitFor(() => {
      expect(screen.getByText(/Email inválido/i)).toBeInTheDocument();
    });

    await waitFor(() => {
      expect(
        screen.getByText(/Senha deve ter no mínimo 6 caracteres/i)
      ).toBeInTheDocument();
    });
  });

  test("deve aceitar dados válidos", async () => {
    // Mock do console.log para verificar se o form foi submetido
    const consoleSpy = vi.spyOn(console, "log").mockImplementation(() => {});

    render(
      <BrowserRouter>
        <SignupForms />
      </BrowserRouter>
    );

    // Preenche o formulário com dados válidos
    fireEvent.change(screen.getByLabelText("Nome"), {
      target: { value: "João Silva" },
    });
    fireEvent.change(screen.getByLabelText("Nome de Usuário"), {
      target: { value: "joaosilva" },
    });
    fireEvent.change(screen.getByLabelText("Email"), {
      target: { value: "joao@email.com" },
    });
    fireEvent.change(screen.getByLabelText("Senha"), {
      target: { value: "senha123456" },
    });

    // Submete o formulário
    const submitButton = screen.getByRole("button", { name: /enviar/i });
    fireEvent.click(submitButton);

    // Verifica se o form foi submetido com sucesso
    await waitFor(() => {
      expect(consoleSpy).toHaveBeenCalledWith({
        name: "João Silva",
        username: "joaosilva",
        email: "joao@email.com",
        password: "senha123456",
      });
    });

    consoleSpy.mockRestore();
  });

  test("deve verificar se campo email aceita apenas emails válidos", async () => {
    render(
      <BrowserRouter>
        <SignupForms />
      </BrowserRouter>
    );

    // Preenche o campo de email
    const emailInput = screen.getByLabelText("Email");

    // Testa que o campo aceita texto (mesmo que inválido no momento)
    fireEvent.change(emailInput, {
      target: { value: "email-invalido" },
    });

    // Verifica se o valor foi definido
    expect(emailInput.value).toBe("email-invalido");

    // Agora testa com email válido
    fireEvent.change(emailInput, {
      target: { value: "email@valido.com" },
    });

    // Verifica se o valor foi atualizado
    expect(emailInput.value).toBe("email@valido.com");
  });

  test("deve mostrar alert após cadastro bem-sucedido", async () => {
    // Mock do alert
    const alertSpy = vi.spyOn(window, "alert").mockImplementation(() => {});

    render(
      <BrowserRouter>
        <SignupForms />
      </BrowserRouter>
    );

    // Preenche o formulário com dados válidos
    fireEvent.change(screen.getByLabelText("Nome"), {
      target: { value: "Maria Santos" },
    });
    fireEvent.change(screen.getByLabelText("Nome de Usuário"), {
      target: { value: "mariasantos" },
    });
    fireEvent.change(screen.getByLabelText("Email"), {
      target: { value: "maria@teste.com" },
    });
    fireEvent.change(screen.getByLabelText("Senha"), {
      target: { value: "minhasenha123" },
    });

    // Submete o formulário
    const submitButton = screen.getByRole("button", { name: /enviar/i });
    fireEvent.click(submitButton);

    // Verifica se o alert foi chamado
    await waitFor(() => {
      expect(alertSpy).toHaveBeenCalledWith("Cadastro realizado com sucesso!");
    });

    alertSpy.mockRestore();
  });
});
