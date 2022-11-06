from flask import url_for
from decimal import *
from ext.db import db
from sqlalchemy.ext.orderinglist import ordering_list
from flask_wtf import FlaskForm
from sqlalchemy.ext.mutable import MutableList
from modules.core.models import BaseModels,ARRAY,JSON,Decimal

class Veiculos(BaseModels):
    pessoa_id = db.Column(db.Integer, db.ForeignKey('pessoa.id'), nullable = True)
    modelo = db.Column(db.String(40))
    cor = db.Column(db.String(40))
    placa = db.Column(db.String(40))
    pessoa = db.relationship('Pessoa', foreign_keys=[pessoa_id] , backref='veiculo_pessoa')