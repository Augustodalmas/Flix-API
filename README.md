# 🔒JWT🔓

Nesta versão do meu projeto, implementei a autenticação para garantir que apenas usuários autenticados possam interagir com a API. A autenticação foi aplicada a todas as views, de forma que somente usuários cadastrados têm permissão para criar, atualizar ou deletar filmes, atores, avaliações e gêneros.

Funcionalidades</br>
Autenticação de Usuários: Utilização de JSON Web Tokens (JWT) para autenticação segura.</br>
Proteção das Views: Todas as operações de criação, atualização e exclusão estão restritas a usuários autenticados.</br>
CRUD Completo: Gerenciamento completo de filmes, atores, avaliações e gêneros, acessível apenas para usuários autenticados.</br>

Tecnologias Utilizadas</br>
Django: Framework principal utilizado para o desenvolvimento da aplicação.</br>
Django REST Framework: Ferramenta utilizada para a construção da API.</br>
JWT (JSON Web Token): Mecanismo de autenticação utilizado para proteger as rotas da API.</br></br>
🚀 Como Executar o Projeto
Clone o repositório:<br>
```git clone https://github.com/Augustodalmas/Flix-API.git```

Navegue até o diretório do projeto:<br>
```cd seu-repositorio```

Crie e ative um ambiente virtual:<br>
```python -m venv venv```<br><br>
```source venv/bin/activate```<br> # No Windows<br> `venv\Scripts\activate`

Instale as dependências:<br>
```pip install -r requirements.txt```

Execute as migrações:<br>
```python manage.py migrate```

Inicie o servidor de desenvolvimento:<br>
```python manage.py runserver```
api/v1/reviews/ - Endpoints para Create e list de reviews.<br>
api/v1/reviews/id/ - Endpoints para Update, Detail e Delete de reviews.<br>
api/v1/actors/ - Endpoints para Create e list de atores.<br>
api/v1/actors/id/ - Endpoints para Update, Detail e Delete de atores.<br>
api/v1/movies/ - Endpoints para Create e list de filmes.<br>
api/v1/movies/id/ - Endpoints para Update, Detail e Delete de filmes.<br>
