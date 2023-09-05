# Configurações de projeto

### Como Usar ? 
```python
from feiticeiro_tec.config.with_dynaconf import TypeEnv


class Environtment(TypeEnv):
    MYENV: str


CONFIG = Environtment.load_env(
    default="DEFAULT",
    env="DEV",
    settings_files=["settings.toml"],
)

CONFIG.show()

```

> settings.toml
```toml
[DEFAULT]
DEBUG=true


[DEV]
MYENV='ola'
```

> console
```log
2023-09-05 04:44:02.298 | WARNING  | feiticeiro_tec.config.with_dynaconf:show:48 - VARIAVEIS DE AMBIENTE: DEV
ENV = EnvEnum.DEV
DEBUG = True
MYENV = ola
_settings = <dynaconf.base.Settings object at 0x7f9dbdd9afd0>
```