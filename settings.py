from flask import current_app


def get_app_var(key):
    return current_app.config.get(key)
