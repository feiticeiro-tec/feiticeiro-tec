from feiticeiro_tec.flask.job_manager import JobManager
from flask import Flask
from multiprocessing import SimpleQueue


def test_new_task():
    app = Flask(__name__)
    app.secret_key = "123"
    jm = JobManager(app)
    processo = jm.tasks.new("TASK TASK BEM AQUI", lambda: print("teste"))

    with app.test_client() as client:
        response = client.post(
            "/jobs/login",
            data={"acesso": "123"},
            follow_redirects=True,
        )
        assert str(processo.uuid) in response.text


def test_run_job():
    app = Flask(__name__)
    app.secret_key = "123"
    jm = JobManager(app)
    hook = SimpleQueue()

    def run():
        hook.put(182653)

    processo = jm.tasks.new(
        "TASK TASK BEM AQUI",
        target=run,
    )

    with app.test_client() as client:
        client.post(
            "/jobs/login",
            data={"acesso": "123"},
            follow_redirects=True,
        )
        x = client.post(f"/jobs/{processo.uuid}/", follow_redirects=True)
        assert x.status_code == 200

    assert hook.get() == 182653
