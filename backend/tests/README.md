# Testes Unitários - SocialJAM Backend

Este diretório contém 10 testes unitários abrangentes para o backend do projeto SocialJAM, cobrindo as funcionalidades das entidades **Album**, **User**, **Artist**.

## Estrutura dos Testes

### 📁 Arquivos Criados

```
tests/
├── __init__.py              # Pacote Python
├── conftest.py              # Configurações e fixtures compartilhadas
└── test_album.py            # 3 testes principais + 2 adicionais para Album
└── test_user.py            # 3 testes principais + 2 adicionais para User
└── test_artist.py            # 3 testes principais + 2 adicionais para Artist
```

## Testes Implementados

### 💿 Album (test_album.py)
1. **test_create_album_success** - Criação bem-sucedida de álbum no modelo
2. **test_create_album_api_success** - Criação de álbum via API
3. **test_get_album_by_name** - Buscar álbum por nome
4. **test_get_nonexistent_album_returns_404** - Buscar álbum inexistente (404)
5. **test_album_artist_relationship** - Relacionamento entre artista e álbuns

### 👤 User (test_user.py)
1. **test_create_user_success** - Criação bem-sucedida de usuário no modelo
2. **test_create_user_api_success** - Criação de usuário via API
3. **test_get_user_by_username** - Buscar usuário por username
4. **test_get_nonexistent_user_returns_404** - Buscar usuário inexistente (404)
5. **test_create_user_with_duplicate_username** - Validação de username único

### 🎵 Artist (test_artist.py)  
4. **test_create_artist_success** - Criação bem-sucedida de artista no modelo
5. **test_create_artist_api_success** - Criação de artista via API
6. **test_get_artist_by_name** - Buscar artista por nome
7. **test_get_nonexistent_artist_returns_404** - Buscar artista inexistente (404)
8. **test_get_all_artists** - Listar todos os artistas

## Como Executar

### Pré-requisitos
- Python 3.13+
- uv (gerenciador de dependências)

### Comandos

```bash
# Navegar para o diretório do backend
cd backend

# Instalar dependências
uv sync

# Executar todos os testes
uv run pytest tests/ -v

# Executar testes específicos
uv run pytest tests/test_user.py -v
uv run pytest tests/test_artist.py -v
uv run pytest tests/test_album.py -v

# Executar com coverage
uv run pytest tests/ --cov=app --cov-report=html
```

## Características dos Testes

### 🛠️ Configuração (conftest.py)
- **Banco de dados de teste em memória** (SQLite)
- **Fixtures reutilizáveis** para dados de exemplo
- **Cliente de teste FastAPI** configurado
- **Isolamento entre testes** (cada teste tem sua própria sessão de banco)

### ✅ Cobertura de Funcionalidades
- **Modelos SQLAlchemy**: Criação e validação de entidades
- **APIs REST**: Endpoints de criação, busca e listagem
- **Relacionamentos**: Associações entre Artist e Album
- **Validações**: Constraints de unicidade e dados obrigatórios
- **Tratamento de Erros**: Casos de erro 404 e validação

### 🎯 Boas Práticas
- **Arrange-Act-Assert**: Estrutura clara nos testes
- **Nomenclatura descritiva**: Nomes explicativos para cada teste
- **Dados isolados**: Cada teste usa dados independentes
- **Múltiplos cenários**: Casos de sucesso e erro
- **Documentação**: Docstrings explicativas

## Resultados

```
================================= 15 passed, 4 warnings in 2.32s =================================
```

Todos os 15 testes passaram com sucesso, garantindo a qualidade e confiabilidade do código backend.

## Dependências de Teste

As seguintes dependências foram utilizadas:
- `pytest` - Framework de testes
- `fastapi[all]` - Cliente de teste para APIs
- `sqlalchemy` - ORM e banco de dados de teste
- `pytest-cov` - Cobertura de código (opcional)

