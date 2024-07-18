# 🔍 Permissions 🔍

Apartir da Flix-Api com Django Rest Framework, consigo aprender um pouco mais sobre permissions do Django.<br>
As permissions assim como o JWT é uma forma de proteger a nossa API e assim definir como cada usuário interage na mesma.<br>
É possivel dentro do Django criar grupos para controlar, como grupo de readonly, admin entre diversas outras opções.<br>
Dentro desse commit, foi adicionado dois métodos de adicionar permissões, 1 método mais hardcode onde seria necessário o desenvolvedor escrever a permissions.py para cada app do API assim ficando muito hardcode.
Para resolver esse problema, dentro do core, foi adicionado uma permissions global, onde ela é dinâmica e se adapta a cada app e a cada model de forma automática.<br>
Ex.:
```
if reviews:
  sum_ratio = 0
  for review in reviews:
    sum_ratio += review.stars
    reviewCount = obj.reviews.count()
  return round(sum_ratio / reviewCount, 1)
return None
```
Onde todo esse trecho de código acaba se transformando em.
```
ratio = obj.reviews.aggregate(Avg('stars'))['stars__avg']
if reviews:
  return round(ratio, 2)
return None
```

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

🔗Endpoints<br>
A API possui os seguintes endpoints principais:<br>

api/v1/genres/ - Endpoints para Create e list de genres.<br>
api/v1/genres/id/ - Endpoints para Update, Detail e Delete de genres.<br>
api/v1/reviews/ - Endpoints para Create e list de reviews.<br>
api/v1/reviews/id/ - Endpoints para Update, Detail e Delete de reviews.<br>
api/v1/actors/ - Endpoints para Create e list de atores.<br>
api/v1/actors/id/ - Endpoints para Update, Detail e Delete de atores.<br>
api/v1/movies/ - Endpoints para Create e list de filmes.<br>
api/v1/movies/id/ - Endpoints para Update, Detail e Delete de filmes.<br>
