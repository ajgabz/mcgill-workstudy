class Config(object):
    DEBUG = False
    TESTING = False
    POSTGRES_CONNECTION_URI = ""

class DevelopmentConfig(Config):
    POSTGRES_CONNECTION_URI = "postgresql://aarongaba@localhost/aarongaba"
    DEBUG = True

class TestingConfig(Config):
    TESTING = True