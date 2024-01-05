# Tipos de Usos


## Job Manager
O job manager ajuda na exibição e execução de funções de forma manual atraves de uma interface web dentro da area de admin do flask.

### Como usar
Primeiro vamos instanciar o app do flask e o flask-admin
```python 
from flask import Flask
from flask_admin import Admin

app = Flask(__name__)
app.secret_key = #Sua Secret
admin = Admin(app, name='App', template_mode='bootstrap3')
```

Agora vamos instanciar o job manager
```python
from feiticeiro_tec.job_manager import JobManager

job_manager = JobManager(app)
```

Agora vamos inicializar as views dentro do flask-admin
> No lugar do lambda informa a sua função de permissao de acesso
```python
job_manager.init_view(lambda: True)
```

Agora vamos criar as taferas que vai ser exibido pelo job manager

```python
#Usando decorador em uma função 
@job_manager.tasks.task()
def test():
    """teste de descrição"""
    print("teste")


```

```python
#Usando o metodo new
job_manager.tasks.new(
    name="nome",
    target=lambda: print("teste"),
    description="teste de descrição"
)
```

Pronto executar flask run e acessar http://localhost:5000/admin/jobs/ vai ser as funções que podem ser executadas manualmente

![imagem da tela](https://github.com/feiticeiro-tec/feiticeiro-tec/assets/53744463/215ac186-a8c5-4843-9cb3-06a0f36fb929)

## Config With Dynaconf
O config with dynaconf ajuda na coleta de variaveis validando o tipo e se é obrigatorio ou não, dessa forma é possivel garantir que todas as envs necessarias para o funcionamento do sistema estejam presentes.

### Como usar
Primeiro vamos definir quais seram nossa variaveis.

```python
from feiticeiro_tec.config.with_dynaconf import TypeEnv

class MyEnv(TypeEnv):
    SECRET_KEY: str
```

agora vamos ler as variaveis, vamos definir qual vai ser o ambiente default, qual ambiente vamos usar no exemplo abaixo estamos usando o ambiente DEV, e iremos ler as variaveis de um arquivo chamado settings.yaml

```yaml
# settings.yaml
DEFAULT:
  debug: false

DEV:
  debug: true
  secret_key: 'dev_secret_key'
```

```python
setting = MyEnv.load_env(
    default="DEFAULT",
    env="DEV",
    settings_files=["settings.yaml"],
)

print(setting.SECRET_KEY) # >> dev_secret_key
print(setting.DEBUG) # >> True
```
> Todas as declareções fica em UPPERCASE para indicar que é uma constante


## RuleRouter
O RuleRouter ajuda na criação de permissões de acesso, baseado na rotas da sua aplicação, ele vai criar uma permissão para rota e method usado, dessa forma é possivel criar permissões de acesso de forma customizada.

### Como usar
Primeiro vamos instanciar o app do flask
```python
from flask import Flask


app = Flask(__name__)
app.secret_key = "secret"
```
como precisamos de um banco de dados para armazenar as permissões vamos instanciar o sqlalchemy
```python
from flask_sqlalchemy import SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)
```
Agora vamos instanciar o RuleRouter
```python
rules = RuleRouter(app, db)
```
Agora vamos criar as rotas que vão ser usadas para criar as permissões
```python
@app.route("/")
def index():
    return "Hello World"
```
Agora vamos iniciar o banco de dados e criar as permissões
```python
with app.app_context():
    db.create_all()
    rules.init_routes()
```
Tambem é possivel colocar as permissoes para exibição dentro do flask-admin, basta inicalizar o flask Admine chamar o init_view e passar a função validação de acesso
```python
from flask_admin import Admin
admin = Admin(app)

rules.init_view(lambda:True)
```
#### Screenshots
> essa é a exibição do endpoint existente
![endpoint](https://github.com/feiticeiro-tec/feiticeiro-tec/assets/53744463/b3bb4997-2f6e-4e56-9df8-b57c4ab221cb)

> esse é a exibição dos methods reconhecidos
![method](https://github.com/feiticeiro-tec/feiticeiro-tec/assets/53744463/fdd88e8d-9d2e-4bdf-9aea-174377281384)

> esse é a exibição da relação de endpoint e method onde é recomendado fazer a relação com a entidade que deve ter a permissão.
![endpoint-method](https://github.com/feiticeiro-tec/feiticeiro-tec/assets/53744463/e9562a0f-d31d-44b7-97dd-463167bae353)

> esse é o diagrama da relação das permissoes.
![diagrama](https://github.com/feiticeiro-tec/feiticeiro-tec/assets/53744463/cb7b1c24-096f-4579-8be7-f7dfe9a34cab)