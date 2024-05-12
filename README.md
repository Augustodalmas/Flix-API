# Django Genres API
Este projeto consiste em uma API simples para gerenciar gêneros de filmes utilizando Django, um framework web em Python. A API permite a criação, listagem, atualização e remoção de gêneros de filmes.

Funcionalidades:
Listagem de Gêneros: Permite visualizar todos os gêneros de filmes existentes.
Criação de Gênero: Possibilita adicionar novos gêneros à base de dados.
Detalhes do Gênero: Fornece informações detalhadas sobre um gênero específico.
Atualização de Gênero: Permite modificar o nome de um gênero existente.
Remoção de Gênero: Permite excluir um gênero da base de dados.

Tecnologias Utilizadas:
Django: Framework web em Python utilizado para desenvolver a API.
Python: Linguagem de programação utilizada para escrever a lógica da aplicação.
JSON: Formato de dados utilizado para comunicação entre o cliente e o servidor.

Estrutura do Projeto:
O projeto é estruturado em torno de duas principais views:

genres_create_list: Responsável por lidar com requisições relacionadas à listagem e criação de gêneros.
genre_detail: Responsável por lidar com requisições relacionadas à obtenção, atualização e remoção de detalhes de um gênero específico.
Além disso, o projeto utiliza a funcionalidade de serialização do Django para converter objetos de modelo em representações JSON e vice-versa.

Como Utilizar:
Clone este repositório em sua máquina local.
Certifique-se de ter o Python e Django instalados em seu ambiente de desenvolvimento.
Execute o servidor Django.
Utilize uma ferramenta como URL, Postman ou Insomnia para realizar requisições HTTP para a API.
