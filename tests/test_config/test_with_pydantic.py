import os
from feiticeiro_tec.config.with_dynaconf import TypeEnv


def test_load_env():
    class Env(TypeEnv):
        TESTE: int
        OLA: str

    env = Env.load_env(
        default="DEFAULT",
        env="DEV",
        settings_files=["tests/test_config/arquivos/teste_env.yaml"],
    )
    assert env.ENV.value == "DEV"
    assert env.DEBUG is False
    assert env.TESTE == 1
    assert env.OLA == "mundo"


def test_load_env_with_env_forte():
    os.environ["TESTE"] = "2"

    class Env(TypeEnv):
        TESTE: int

    env = Env.load_env(
        default="DEFAULT",
        env="DEV",
        settings_files=["tests/test_config/arquivos/teste_env.yaml"],
    )
    assert env.ENV.value == "DEV"
    assert env.DEBUG is False
    assert env.TESTE == 2


def test_load_env_with_objeto():
    os.environ.pop("TESTE", None)

    class Env(TypeEnv):
        TESTE: int
        OBJETO: dict

    env = Env.load_env(
        default="DEFAULT",
        env="DEV",
        settings_files=["tests/test_config/arquivos/teste_env.yaml"],
    )
    assert env.ENV.value == "DEV"
    assert env.DEBUG is False
    assert env.TESTE == 1
    assert env.OBJETO == {"x": 2, "y": "Y"}
