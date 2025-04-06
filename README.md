✅ COMO RODAR O PROJETO

## Estrutura dos repositórios
- 🔙 Backend (este repositório)
- 🔜 Frontend: [Link para o repositório do frontend]([https://github.com/seu-usuario/frontend-repo](https://github.com/gabrielguady/frontend-desafio.git))

⚠️ PASSO 1: Ajustar caminhos no docker-compose.yml
No arquivo backend/docker-compose.yml, troque:
build:
  context: 'C:/CAMINHO/ATUAL/DO/BACKEND'
volumes:
  - C:/CAMINHO/ATUAL/DO/BACKEND:/app
frontend:
  build:
    context: 'C:/CAMINHO/ATUAL/DO/FRONTEND'
  volumes:
    - C:/CAMINHO/ATUAL/DO/FRONTEND:/app
   
⚙️ PASSO 2: Subir com Docker
cd backend
docker-compose up --build

✅ FUNCIONAMENTO
 coloque essa url no seu browser: http://localhost:4200

 🧪 Testes
 docker-compose exec backend pytest
