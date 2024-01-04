from feiticeiro_tec.flask.rule_router import RuleRouter
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin


def test_rule_router():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db = SQLAlchemy(app)
    rules = RuleRouter(app=app, db=db)

    assert rules.app == app
    assert rules.app.extensions["rule_router"] == rules
    assert rules.db == db


def test_rule_router_init_permissions():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    db = SQLAlchemy(app)
    rules = RuleRouter(app=app, db=db)

    @app.route("/")
    def index():
        return "Hello World!"

    with app.app_context():
        db.create_all()

    rules.init_permissions()
    with app.app_context():
        rotas = rules.Router.query.all()
        assert len(rotas) == 1
        assert rotas[0].endpoint == "index"
        assert rotas[0].uri == "/"
        assert rotas[0].subdomain == ""
        assert rotas[0].description is None
        assert rotas[0].active is True

        rotas_metodos = rules.RouterMethod.query.all()
        assert len(rotas_metodos) == 1
        assert rotas_metodos[0].router_endpoint == "index"
        assert rotas_metodos[0].method_rule == "GET"
        assert rotas_metodos[0].active is True

        metodos = rules.Method.query.all()
        assert len(metodos) == 1
        assert metodos[0].rule == "GET"


def test_rule_router_init_view():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    Admin(app, name="Teste", template_mode="bootstrap3")
    db = SQLAlchemy(app)

    rules = RuleRouter(app=app, db=db)

    @app.route("/")
    def index():
        return "Hello World!"

    with app.app_context():
        db.create_all()

    rules.init_view()

    with app.test_client() as client:
        response = client.get("/admin/", follow_redirects=True)
        assert "Permissions" in response.text
        assert "Router" in response.text
        assert "Router Method" in response.text
        assert "Method" in response.text

    with app.test_client() as client:
        response = client.get("/admin/router/", follow_redirects=True)
        assert response.status_code == 200

        response = client.get("/admin/routermethod/", follow_redirects=True)
        assert response.status_code == 200

        response = client.get("/admin/method/", follow_redirects=True)
        assert response.status_code == 200


def test_rule_router_init_view_permission():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    Admin(app, name="Teste", template_mode="bootstrap3")
    db = SQLAlchemy(app)

    rules = RuleRouter(app=app, db=db)

    @app.route("/")
    def index():
        return "Hello World!"

    with app.app_context():
        db.create_all()

    rules.init_view(lambda: False)

    with app.test_client() as client:
        response = client.get("/admin/", follow_redirects=True)
        assert "Permissions" not in response.text
        assert "Router" not in response.text
        assert "Router Method" not in response.text
        assert "Method" not in response.text

    with app.test_client() as client:
        response = client.get("/admin/router/", follow_redirects=True)
        assert response.status_code == 403

        response = client.get("/admin/routermethod/", follow_redirects=True)
        assert response.status_code == 403

        response = client.get("/admin/method/", follow_redirects=True)
        assert response.status_code == 403
