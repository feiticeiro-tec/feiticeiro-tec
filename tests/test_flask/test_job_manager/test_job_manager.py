from feiticeiro_tec.flask.job_manager import JobManager
from flask import Flask
from flask_admin import Admin


def test_init_app():
    app = Flask(__name__)
    job_manager = JobManager(app)
    assert app.extensions["job_manager"] == job_manager


def test_login():
    app = Flask(__name__)
    app.secret_key = "123"
    Admin(app)
    jm = JobManager(app)
    jm.init_view(lambda: False)
    with app.test_client() as client:
        response = client.get("/admin/jobs/")
        assert response.status_code == 403
