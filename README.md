# 🎬API de Filmes com Django🎥

Este repositório contém uma API de gerenciamento de filmes desenvolvida com Django.
A API permite realizar operações CRUD (Create, Read, Update, Delete) para diversas entidades relacionadas a filmes, incluindo gêneros, reviews, atores e os próprios filmes.

📚Funcionalidades:
🎭Gêneros
Create: Adicione novos gêneros de filmes.
List: Consulte a lista completa de gêneros cadastrados.
Detail: Visualize informações detalhadas sobre um gênero específico.
Update: Edite as informações de um gênero existente.
Delete: Remova um gênero do sistema.

📝Reviews
Create: Adicione novas reviews para filmes.
List: Consulte todas as reviews cadastradas.
Detail: Visualize informações detalhadas sobre uma review específica.
Update: Edite as informações de uma review existente.
Delete: Remova uma review do sistema.

🎭Atores
Create: Adicione novos atores ao banco de dados.
List: Consulte a lista completa de atores cadastrados.
Detail: Visualize informações detalhadas sobre um ator específico.
Update: Edite as informações de um ator existente.
Delete: Remova um ator do sistema.

🎬Filmes
Create: Adicione novos filmes ao banco de dados.
List: Consulte a lista completa de filmes cadastrados.
Detail: Visualize informações detalhadas sobre um filme específico.
Update: Edite as informações de um filme existente.
Delete: Remova um filme do sistema.

🛠Tecnologias Utilizadas:
Django: Framework web utilizado para construir a API.
Django REST Framework: Biblioteca poderosa e flexível para construir APIs Web em Django.
SQLite: Banco de dados utilizado para armazenamento de dados.

🚀 Como Executar o Projeto Clone o repositório:
git clone https://github.com/Augustodalmas/Flix-API.git

Navegue até o diretório do projeto:
cd seu-repositorio

Crie e ative um ambiente virtual:
python -m venv venv

source venv/bin/activate
No Windows
venv\Scripts\activate

Instale as dependências:
pip install -r requirements.txt

Execute as migrações:
python manage.py migrate

Inicie o servidor de desenvolvimento:
python manage.py runserver

🔗Endpoints
A API possui os seguintes endpoints principais:

api/v1/genres/ - Endpoints para Create e list de genres.
api/v1/genres/id/ - Endpoints para Update, Detail e Delete de genres.
api/v1/reviews/ - Endpoints para Create e list de reviews.
api/v1/reviews/id/ - Endpoints para Update, Detail e Delete de reviews.
api/v1/actors/ - Endpoints para Create e list de atores.
api/v1/actors/id/ - Endpoints para Update, Detail e Delete de atores.
api/v1/movies/ - Endpoints para Create e list de filmes.
api/v1/movies/id/ - Endpoints para Update, Detail e Delete de filmes.
