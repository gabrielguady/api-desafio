✅ COMO RODAR O PROJETO

## Estrutura dos repositórios
- 🔙 Backend (este repositório)
- 🔜 Frontend: https://github.com/gabrielguady/frontend-desafio.git

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


TEM QUE SER O PATH DE ONDE ESTÁ A PASTA


⚙️ PASSO 2: Subir com Docker

cd backend

docker-compose up --build



✅ FUNCIONAMENTO

 coloque essa url no seu browser: http://localhost:4200/calcular

 🧪 Testes

 execute esse comando no terminal docker: 
 
 docker-compose exec backend pytest
