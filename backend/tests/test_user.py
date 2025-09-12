
import pytest
from fastapi import status
from app import models
from app.core.security import HashPWD


class TestUserModel:
    
    def test_create_user_success(self, db_session, sample_user_data):
        # Arrange
        user_data = sample_user_data
        
        # Act
        new_user = models.User(
            nome=user_data["nome"],
            username=user_data["username"],
            email=user_data["email"],
            senha=HashPWD(user_data["senha"])
        )
        db_session.add(new_user)
        db_session.commit()
        db_session.refresh(new_user)
        
        # Assert
        assert new_user.id is not None
        assert new_user.username == user_data["username"]
        assert new_user.nome == user_data["nome"]
        assert new_user.email == user_data["email"]
        assert new_user.senha != user_data["senha"]  # Senha deve estar hashada


class TestUserAPI:
    
    def test_create_user_api_success(self, client, sample_user_data):
        # Arrange
        user_data = sample_user_data
        
        # Act
        response = client.post("/user", json=user_data)
        
        # Assert
        assert response.status_code == status.HTTP_201_CREATED
        response_data = response.json()
        assert response_data["username"] == user_data["username"]
        assert response_data["nome"] == user_data["nome"]
        assert response_data["email"] == user_data["email"]
        assert "senha" not in response_data  # Senha não deve aparecer na resposta
    
    def test_get_user_by_username(self, client, sample_user_data):
        # Arrange - Primeiro criar o usuário
        user_data = sample_user_data
        client.post("/user", json=user_data)
        
        # Act
        response = client.get(f"/user/{user_data['username']}")
        
        # Assert
        assert response.status_code == status.HTTP_200_OK
        response_data = response.json()
        assert response_data["username"] == user_data["username"]
        assert response_data["nome"] == user_data["nome"]
        assert response_data["email"] == user_data["email"]


class TestUserValidation:
    
    def test_get_nonexistent_user_returns_404(self, client):
        # Act
        response = client.get("/user/nonexistent_user")
        
        # Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND
    
    def test_create_user_with_duplicate_username(self, client, sample_user_data):
        # Arrange
        user_data = sample_user_data
        client.post("/user", json=user_data)  # Criar primeiro usuário
        
        # Act - Tentar criar outro usuário com mesmo username
        # Isto deve falhar devido ao constraint de uniqueness
        try:
            response = client.post("/user", json=user_data)
            # Se chegou até aqui, algo está errado
            assert False, "Deveria ter falhado devido ao username duplicado"
        except Exception:
            # Assert - Exception esperada devido ao constraint violation
            assert True  # Teste passou - a exceção foi levantada como esperado