import logging
from datetime import timedelta
import os

basedir = os.getcwd()
class Config:
    DEBUG = False
    APP=os.environ.get('APP_NAME',"APP")
    LINK_COPYRIGHT = os.environ.get('LINK_COPYRIGHT',"#")
    POSTGRES = {
        'db': os.environ['POSTGRES_DATABASE'],
        'user': os.environ['POSTGRES_USER'],
        'pw': os.environ['POSTGRES_PASSWORD'],
        'host': os.environ['POSTGRES_HOST'],
        'port': os.environ['POSTGRES_PORT'],
    }
    REDIS_URL = {
        'host': os.environ.get('REDIS_HOST','redis'),
        'porta': os.environ.get('REDIS_PORTA','6379'),
        'db': os.environ.get('REDIS_BASE','0'),
    }
    SECRET_KEY = os.environ.get('SECRET_KEY',"")
    REDIS_URL = 'redis://%(host)s:%(porta)s/%(db)s' % REDIS_URL
    USE_TZ = True
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_ECHO = False  
    MEDIUM_DATE = "EEEE, d. MMMM y 'at' HH:mm"
    FULL_DATE = "EE dd.MM.y HH:mm"
    LOG_FORMAT = "%(asctime)s %(levelname)s\t: %(message)s"
    BABEL_DEFAULT_LOCALE = 'pt_BR'
    SECURITY_MSG_LOGIN=("", "")
    SECURITY_UNIFIED_SIGNIN= True
    SQLALCHEMY_ENGINE_OPTIONS = {
      "pool_pre_ping": True,
      "pool_recycle": 300,
    }
    SECURITY_PASSWORD_SALT= "Password@1"
    SECURITY_LOGIN_USER_TEMPLATE="/auth/login.html"
    SECURITY_MSG_INVALID_PASSWORD = ("Usuário ou senha invalida", "error")
    SECURITY_USER_IDENTITY_ATTRIBUTES = ('username')
    SECURITY_MSG_INVALID_PASSWORD = ("Usuário ou senha invalida", "error")
    SECURITY_MSG_PASSWORD_NOT_PROVIDED = ("Usuário ou senha invalida", "error")
    SECURITY_MSG_USER_DOES_NOT_EXIST = ("Usuário ou senha invalida", "error")
    SECURITY_MSG_UNAUTHORIZED=("Você não tem permissão para acessar esse recurso.\ncontacte o administrador do sistema!","info")

class DevelopmentConfig(Config):
    FLASK_ENV ='development'
    DEBUG = True
    SQLALCHEMY_ECHO = False

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    SERVER_NAME='localhost'
    POSTGRES = {
        'db': 'testing_{0}'.format(os.environ['POSTGRES_USER']),
        'user': os.environ['POSTGRES_USER'],
        'pw': os.environ['POSTGRES_PASSWORD'],
        'host': os.environ['POSTGRES_HOST'],
        'port': os.environ['POSTGRES_PORT'],
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    TESTING = True
    DEBUG=False
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED=False
    SQLALCHEMY_ECHO = False

config = {
    None: DevelopmentConfig,
    'dev': DevelopmentConfig,
    'prod': ProductionConfig,
    'test': TestingConfig
}
