from flask import url_for
from decimal import *
from ext.db import db
from sqlalchemy.ext.orderinglist import ordering_list
from flask_wtf import FlaskForm
from sqlalchemy.ext.mutable import MutableList
from modules.core.models import BaseModels,ARRAY,JSON,Decimal

class Pessoa(BaseModels):
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telefone = db.Column(db.String(255))
    cpf = db.Column(db.String(255))