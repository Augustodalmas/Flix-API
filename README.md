# API de Filmes com Django
Este repositório contém uma API de gerenciamento de filmes desenvolvida com Django. A API permite realizar operações CRUD (Create, Read, Update, Delete) para diversas entidades relacionadas a filmes, incluindo gêneros, reviews, atores e os próprios filmes.

Funcionalidades
Gêneros
Criar: Adicione novos gêneros de filmes.
Listar: Consulte a lista completa de gêneros cadastrados.
Detalhar: Visualize informações detalhadas sobre um gênero específico.
Atualizar: Edite as informações de um gênero existente.
Excluir: Remova um gênero do sistema.
Reviews
Criar: Adicione novas reviews para filmes.
Listar: Consulte todas as reviews cadastradas.
Detalhar: Visualize informações detalhadas sobre uma review específica.
Atualizar: Edite as informações de uma review existente.
Excluir: Remova uma review do sistema.
Atores
Criar: Adicione novos atores ao banco de dados.
Listar: Consulte a lista completa de atores cadastrados.
Detalhar: Visualize informações detalhadas sobre um ator específico.
Atualizar: Edite as informações de um ator existente.
Excluir: Remova um ator do sistema.
Filmes
Criar: Adicione novos filmes ao banco de dados.
Listar: Consulte a lista completa de filmes cadastrados.
Detalhar: Visualize informações detalhadas sobre um filme específico.
Atualizar: Edite as informações de um filme existente.
Excluir: Remova um filme do sistema.
Tecnologias Utilizadas
Django: Framework web utilizado para construir a API.
Django REST Framework: Biblioteca poderosa e flexível para construir APIs Web em Django.
SQLite: Banco de dados utilizado para armazenamento de dados.
Como Executar o Projeto
Clone o repositório:
bash
Copiar código
git clone https://github.com/seu-usuario/seu-repositorio.git
Navegue até o diretório do projeto:
bash
Copiar código
cd seu-repositorio
Crie e ative um ambiente virtual:
bash
Copiar código
python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instale as dependências:
bash
Copiar código
pip install -r requirements.txt
Execute as migrações:
bash
Copiar código
python manage.py migrate
Inicie o servidor de desenvolvimento:
bash
Copiar código
python manage.py runserver
Endpoints
A API possui os seguintes endpoints principais:

/api/genres/ - Endpoints para CRUD de gêneros.
/api/reviews/ - Endpoints para CRUD de reviews.
/api/actors/ - Endpoints para CRUD de atores.
/api/movies/ - Endpoints para CRUD de filmes.
