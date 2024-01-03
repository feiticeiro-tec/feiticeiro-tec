from feiticeiro_tec.flask.compress import Compress
from flask import Flask
import gzip
import json


def test_init_app():
    app = Flask(__name__)
    comp = Compress(app)

    assert comp.app == app


def test_not_compress():
    app = Flask(__name__)
    Compress(app)

    @app.route("/")
    def index():
        return {"x": 1}

    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json == {"x": 1}


def test_compress():
    app = Flask(__name__)
    Compress(app)

    @app.route("/")
    def index():
        return {"x": 1}

    with app.test_client() as client:
        response = client.get("/", headers={"Accept-Encoding": "gzip"})
        assert response.status_code == 200
        assert json.loads(gzip.decompress(response.data)) == {"x": 1}
