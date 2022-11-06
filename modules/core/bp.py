import uuid
from datetime import datetime
from ext.db import db
from flask import Blueprint, Flask, Response, render_template,session, request, jsonify,redirect,url_for,flash,g,session
from flask_security import login_required
from sqlalchemy import func,JSON,cast,or_,String,and_,bindparam,literal,update,select,cast,text
from flask_login import fresh_login_required
from modules.core.auth.views import routes as routes_auth
from modules.core.veiculos.views import routes as routes_veiculos
from modules.core.pessoa.views import routes as routes_pessoa

bp = Blueprint('core', __name__,template_folder='templates')

@bp.before_request
@login_required
def before_request():
    pass


@bp.route('/' ,methods=['GET'])
def home():
    return render_template('index.html',q=[])

def init_app(app:Flask, url_prefix=''):
    routers = (routes_auth + routes_veiculos + routes_pessoa )
    for r in routers:
        bp.add_url_rule(r['rule'],endpoint=r.get('endpoint', None),view_func=r['view_func'],**r.get('options', {}))
    app.register_blueprint(bp,url_prefix=url_prefix)
    