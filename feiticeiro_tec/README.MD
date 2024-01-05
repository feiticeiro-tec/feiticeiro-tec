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
