import click,time
from flask import Flask
from .db import db
from flask_security.utils import encrypt_password,url_for_security
from modules.core.auth.models import User,Role

def init_app(app:Flask):
    
    @app.cli.command()
    def initdb():
        db.create_all()

       


