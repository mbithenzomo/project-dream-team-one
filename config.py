class Config(object):
    """
    Default configurations
    """

    TESTING = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# You can include a TestingConfig class as well for running your tests.
# This is however outside the scope of this tutorial.

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
