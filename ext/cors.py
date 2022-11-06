from flask import Flask
from flask_cors import CORS

def init_app(app: Flask):
    CORS(app)
