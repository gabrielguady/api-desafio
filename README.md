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


TEM QUE SER O PATH DE ONDE ESTÁ A PASTA DO PROJETO


⚙️ PASSO 2: Subir com Docker

cd backend

docker-compose up --build



✅ FUNCIONAMENTO

 coloque essa url no seu browser: http://localhost:4200/calcular

 🧪 Testes

 execute esse comando no terminal docker: 
 
 docker-compose exec backend pytest


✅ FUNCIONALIDADE IMPLEMENTADA
📦 Backend (Django + Celery + RabbitMQ)
Endpoints:

POST /processar: recebe três números e inicia o processamento assíncrono (média e mediana).

GET /status/{id}: retorna o status atual do processamento, incluindo status, media, mediana e os três números originais.

Assíncrono com Celery:

Task é enfileirada no RabbitMQ.

O worker processa os dados e atualiza o status no banco (de "Processando..." para "Concluído").

Banco de dados: PostgreSQL na porta 5433.

Gerenciamento: Migrations automáticos no entrypoint (command do Docker).

Exposição: Porta 8000 no host local.

🎨 Frontend (Angular standalone + Angular Material)
Formulário com 3 campos (numero1, numero2, numero3) e botão de envio.

Ao enviar:

O item é adicionado na tabela imediatamente com status "Processando...".

Após 3 segundos, a média e a mediana são buscadas e atualizadas na tabela.

A tabela sempre mostra os números originais enviados e o status atualizado ("Concluído").

A atualização da tabela é feita sem reload da página.

Integração limpa usando @ViewChild pra chamar a função search() do componente filho (EstatisticasListComponent).
