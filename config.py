import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    A class for managing and accessing configuration settings.

    Attributes:
        SPEACH_FILE_PATH (str): The file path for the speech file.
        OPENAI_API_KEY (str): The API key for the OpenAI service.
        SQLALCHEMY_DATABASE_URI (str): The URI for the SQLAlchemy database.
        GOOGLE_CALENDAR_API_SCOPE (list): The scope for the Google Calendar API.
        GOOGLE_OAUTH2_TOKEN_PATH (str): The file path for the Google OAuth2 token.
        GOOGLE_CLIENT_SECRET_FILE_PATH (str): The file path for the Google client secret.
        AUTH_FLOW_LOCAL_SERVER_PORT (int): The local server port for the authorization flow.
        XI_API_KEY (str): The API key for the XI service.

    Methods:
        init_app: Initializes the configuration settings for the given app.
    """
    # File paths
    SPEACH_FILE_PATH = os.path.join(basedir, os.path.join('resources', 'speech.mp3'))

    # OpenAI
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    # Google
    GOOGLE_CALENDAR_API_SCOPE = ['https://www.googleapis.com/auth/calendar.readonly']
    GOOGLE_OAUTH2_TOKEN_PATH = os.path.join(basedir, os.path.join('credentials/google', 'token.json'))
    GOOGLE_CLIENT_SECRET_FILE_PATH = os.path.join(basedir, os.path.join('credentials/google', 'credentials.json'))
    AUTH_FLOW_LOCAL_SERVER_PORT = 0

    XI_API_KEY = os.environ.get('XI_API_KEY')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    FLASK_CONFIG = "DEV"
    TESTING = True
    DEBUG = True


class TestingConfig(Config):
    FLASK_CONFIG = "TEST"
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    FLASK_CONFIG = "STAGING"
    TESTING = False
    DEBUG = False


class ProductionConfig(Config):
    FLASK_CONFIG = "PROD"
    TESTING = False
    DEBUG = False


config = {
    "DEV": DevelopmentConfig,
    "TEST": TestingConfig,
    "STAGING": StagingConfig,
    "PROD": ProductionConfig,
    "default": DevelopmentConfig,
}
