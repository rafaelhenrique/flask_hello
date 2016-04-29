import logging

from flask import Flask

from flask_hello import config
from flask_hello.core import core


def create_app(config=config.prod_config):
    app = Flask("flask_hello")
    app.config.from_object(config)

    register_blueprints(app)
    register_errorhandlers(app)
    register_jinja_env(app)
    register_extensions(app)
    register_logging(app)

    return app


def register_blueprints(app):
    app.register_blueprint(core, url_prefix='/')


def register_errorhandlers(app):
    def render_error(e):
        if e.code == 400:
            return 'Bad request.', 400
        elif e.code == 404:
            return 'Not found.', 404
        elif e.code == 500:
            return 'Internal server error', 500

    for e in [400, 404, 500]:
        app.errorhandler(e)(render_error)


def register_logging(app):

    # Adding file handler on log
    app.logger.addHandler(file_handler('flask_hello.log', 52428800, 1))

    # Adding console handler on log
    app.logger.addHandler(console_handler())


def register_jinja_env(app):
    pass


def register_extensions(app):
    pass


def file_handler(filename, maxbytes, backupcount):
    # Setting handler
    file_handler = logging.handlers.RotatingFileHandler(
        filename=filename,
        maxBytes=maxbytes,  # 50 MB
        backupCount=backupcount,
        )
    file_handler.setLevel(logging.INFO)

    # Setting format of log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    return file_handler


def console_handler():
    # Setting handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Setting format of log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)

    return console_handler
