from flask import Flask,jsonify
from . import handles
from .security import ExtendedLoginForm,ExtendedRegisterForm
from modules.core import bp as core

def init_bps(app:Flask):
    handles.init_app(app)
    core.init_app(app,url_prefix='/')
