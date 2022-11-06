from flask import Flask
from flask_wtf.csrf import CSRFProtect
from . import cors
from ext.db import db
from . import migrate
from . import commands
from ext.security import context_security
from ext.jinja2 import global_vars_templates
from flask_babel import Babel,Locale


def inicialize_libs(app:Flask):
    babel = Babel()
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db)
    commands.init_app(app)
    CSRFProtect(app)
    Babel(app)
    global_vars_templates(app)
    context_security(app)
    