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
