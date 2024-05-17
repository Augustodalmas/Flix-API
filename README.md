# 🎥 Django Genres API 🎬
Descrição 📖<br>
Bem-vindo à Django Genres API! Este projeto oferece uma API RESTful simples e eficiente para gerenciar gêneros de filmes, construída com o poderoso framework Django. Com esta API, você pode criar, listar, atualizar e deletar gêneros filmes com facilidade.<br><br>

Funcionalidades ✨<br>
📜 Listagem de Gêneros: Obtenha uma lista completa de todos os gêneros de filmes disponíveis.<br>
➕ Criação de Gênero: Adicione novos gêneros de filmes à sua coleção.<br>
🔍 Detalhes do Gênero: Visualize informações detalhadas de um gênero específico.<br>
✏️ Atualização de Gênero: Atualize o nome de um gênero existente.<br>
🗑️ Remoção de Gênero: Delete um gênero da base de dados.<br><br>

Tecnologias Utilizadas 🛠️<br>
Django: Framework web em Python que oferece uma estrutura robusta e escalável.<br>
Python: Linguagem de programação utilizada para desenvolver a lógica da aplicação.<br>
JSON: Formato de intercâmbio de dados leve e fácil de usar para comunicação cliente-servidor.<br><br>

Estrutura do Projeto 🏗️<br>
O projeto possui duas principais views:<br>

genres_create_list:<br>

GET: Retorna uma lista de todos os gêneros.<br>
POST: Cria um novo gênero com base nos dados fornecidos.<br><br>

genre_detail:<br>
GET: Retorna os detalhes de um gênero específico.<br>
PUT: Atualiza o nome de um gênero específico.<br>
DELETE: Remove um gênero da base de dados.<br><br>

Como Utilizar 🚀<br>
Clone o Repositório:<br>
```git clone https://github.com/seu-usuario/django-genres-api.git```

Instale as Dependências:<br>
Certifique-se de ter o Python e Django instalados. Em seguida, instale as dependências:<br>
```pip install -r requirements.txt```

Execute as Migrações:<br>
```python manage.py migrate```

Inicie o Servidor Django:<br>
```python manage.py runserver```
