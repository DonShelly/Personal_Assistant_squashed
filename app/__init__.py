import logging.config
import os

from flask import Flask

from app.extensions import db, ma
from app.log import LOG_CONFIG
from config import config

logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)

log_levels = {
    "DEBUG": logging.DEBUG,
    "INFO": logging.INFO,
    "WARNING": logging.WARNING,
    "ERROR": logging.ERROR,
    "CRITICAL": logging.CRITICAL,
}

logger.level = log_levels.get(os.environ.get("LOG_LEVEL", "INFO"))


def init_config(app, config_name):
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)


def init_extensions(app):
    ma.init_app(app)


def init_routes(app):
    from app.routes import routes

    routes.init_routes(app)


def create_app(config_name):
    app = Flask(__name__)

    init_config(app, config_name)
    init_extensions(app)
    init_routes(app)

    return app
