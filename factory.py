from flask import Flask,render_template,redirect,url_for
from ext.config import Config,config
from ext.bps import init_bps
from ext.libs import inicialize_libs

def create_app(settings=None) -> Flask:
    app = Flask(__name__)
    cfg = config[settings]
    app.config.from_object(cfg)
    inicialize_libs(app)
    init_bps(app)
    return app