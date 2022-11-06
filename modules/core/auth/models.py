from flask import url_for
from ext.db import db
from decimal import *
from modules.core.models import BaseModels,ARRAY,JSON,Decimal
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(BaseModels, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(BaseModels, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255),unique=True)
    email_confirmacao = db.Column(db.String(255))
    password = db.Column(db.String(255))
    session = db.Column(db.String(2555555))
    nome_completo = db.Column(db.String(400))
    cpf_cnpj = db.Column(db.String(20))
    celular = db.Column(db.String(20))
    rg = db.Column(db.String(40))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users,backref=db.backref('users', lazy='dynamic'))

    def has_role(self, role):
        return role in self.roles