from flask import url_for
import uuid
import sqlalchemy
from ext.db import db
from sqlalchemy import event,inspect,PickleType 
from decimal import *
from sqlalchemy.ext.mutable import MutableList,Mutable
from sqlalchemy.dialects.postgresql import ARRAY,JSON
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from sqlalchemy.types import TypeDecorator
from sqlalchemy.ext.mutable import MutableDict, Mutable

class BaseModels(db.Model):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer(), primary_key=True)
    ativo = db.Column(db.Boolean, default=True)
    data_criacao = db.Column(db.DateTime, default=db.func.now())
    data_atualizacao = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
