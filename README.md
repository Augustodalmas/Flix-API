# 🔍 Serializers 🔍

Apartir da Flix-Api com Django Rest Framework, foi possivel se aprofundar no assunto Serializers.<br>
Serializer entra em nosso projeto com intuito de validar, calcular, estruturar e serializar os dados no formato Json.<br>
Temos como exemplo neste repositório formas mais braçais de realizar operações com serializer e logo em seguida uma forma mais prática.<br>
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
