import os


class Config(object):   # 所有配置類的父類，通用的配寫在這裡
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    url = os.environ.get('DATABASE_URL')
    if url is not None:
        url = url.split('postgres://')[1]
        SQLALCHEMY_URL = 'postgresql+psycopg2://{}'.format(url)
    ENV = 'development'


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}