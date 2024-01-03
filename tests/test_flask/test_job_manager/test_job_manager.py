from feiticeiro_tec.flask.job_manager import JobManager
from flask import Flask


def test_init_app():
    app = Flask(__name__)
    app.secret_key = "123"
    job_manager = JobManager(app)
    assert app.extensions["job_manager"] == job_manager
    assert job_manager.password_key == app.secret_key


def test_endpoint_seguro():
    app = Flask(__name__)
    app.secret_key = "123"
    JobManager(app)
    with app.test_client() as client:
        response = client.get("/jobs/")
        assert response.status_code == 302
        assert response.location == "/jobs/login/"


def test_login():
    app = Flask(__name__)
    app.secret_key = "123"
    JobManager(app)
    with app.test_client() as client:
        response = client.get("/jobs/login/")
        assert response.status_code == 200

    with app.test_client() as client:
        response = client.post("/jobs/login/", data={"acesso": "123"})
        assert response.status_code == 302
        assert response.location == "/jobs/"
        assert client.get("/jobs/").status_code == 200
