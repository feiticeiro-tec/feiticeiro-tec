from flask import (
    Flask,
    render_template,
    request,
    render_template_string,
)
from flask.blueprints import Blueprint
from .jobs import ManagerProcess
from flask_admin import Admin, BaseView, expose
from typing import Callable


class JobManager:
    tasks = ManagerProcess()
    render_template = render_template
    render_template_string = render_template_string

    def __init__(self, app: Flask = None, is_accessible: Callable = None):
        if app:
            self.init_app(app=app, is_accessible=is_accessible)

    def init_app(self, app: Flask, is_accessible: Callable = None):
        self.app = app
        app.extensions["job_manager"] = self
        self.blueprint = self.create_blueprint()
        app.register_blueprint(self.blueprint)
        self.init_view(is_accessible)
        return self

    def init_view(self, is_accessible):
        admin = self.app.extensions.get("admin")
        if not admin:
            admin = Admin(
                app=self.app,
                name=self.app.name,
                template_mode="bootstrap3",
            )
        else:
            admin = admin[0]
        admin.add_view(self.get_view(is_accessible))

    def get_view(self, is_accessible: Callable = None):
        jm = self

        if not is_accessible:
            is_accessible = lambda: True  # noqa

        class JobsViews(BaseView):
            def is_accessible(self):
                return is_accessible()

            @expose("/", methods=("GET",))
            @expose("/<uuid:uuid>/", methods=("POST", "DELETE"))
            def index(self, uuid=None):
                jm.render_template = self.render
                return jm.jobs(uuid=uuid)

        return JobsViews(name="Jobs", endpoint="jobs")

    def jobs(self, uuid=None):
        if request.method == "DELETE":
            self.tasks.stop(uuid)
            return self.render_template("/job_manager/reload.html")
        elif request.method == "POST":
            self.tasks.restart(uuid)
            return self.render_template("/job_manager/reload.html")
        data = {"jobs": tuple(self.tasks)}
        return self.render_template("/job_manager/index.html", data=data)

    def register_blueprint(self, blueprint: Blueprint):
        self.app.register_blueprint(blueprint)

    def create_blueprint(self, url_prefix="/jobs"):
        blueprint = Blueprint(
            "job_manager",
            __name__,
            url_prefix=url_prefix,
            template_folder="templates",
        )
        return blueprint
