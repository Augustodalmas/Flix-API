# 🔍 Permissions 🔍

Apartir da Flix-Api com Django Rest Framework, consigo aprender um pouco mais sobre permissions do Django.<br>
As permissions assim como o JWT é uma forma de proteger a nossa API e assim definir como cada usuário interage na mesma.<br>
É possivel dentro do Django criar grupos para controlar, como grupo de readonly, admin entre diversas outras opções.<br>
Dentro desse commit, foi adicionado dois métodos de adicionar permissões, 1 método mais hardcode onde seria necessário o desenvolvedor escrever a permissions.py para cada app do API assim ficando muito hardcode.<br>
Para resolver esse problema, dentro do core, foi adicionado uma permissions global, onde ela é dinâmica e se adapta a cada app e a cada model de forma automática.<br>
Essa seria a forma automática de verificar as permissões:
```
class globalPermissions(permissions.BasePermission):

    def has_permission(self, request, view):  # Função para lançar o código pronto para verificação na view.
        codename = self._get_codename(method=request.method, view=view)
        if not codename:
            return None
        return request.user.has_perm(codename)

    def _get_codename(self, method, view):  # Função para pegar o código que será enviado ao has_permission.
        try:
            model_name = view.queryset.model._meta.model_name
            app_name = view.queryset.model._meta.app_label
            action = self._get_action(method)
            return f'{app_name}.{action}_{model_name}'
        except AttributeError:
            return None

    def _get_action(self, method):  # Função para pegar a ação do código se baseando no método da requisição.
        method_Actions = {
            "GET": 'view',
            "OPTIONS": 'view',
            "HEAD": 'view',
            "POST": 'add',
            "PATCH": 'change',
            "PUT": 'change',
            "DELETE": 'delete',
        }
        return method_Actions.get(method, "")
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
