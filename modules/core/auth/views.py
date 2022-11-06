from ext.db import db
import requests,json
from functools import wraps
from flask_login import current_user
from modules.core.auth.forms import UserForm,UserFormResetPassword
from modules.core.auth.models import User,Role
from flask_security.decorators import roles_required,roles_accepted
from flask_security.utils import encrypt_password,url_for_security
from flask import render_template, request, jsonify,redirect,url_for,flash,g,abort ,current_app as app
from modules.core.messages import *

routes = []

permissoes = [
    {'name':'lista_usuarios','description':'VISUALIZA USUARIO'},
    {'name':'criacao_usuario','description':'CRIAR USUARIO'},
    {'name':'edicao_usuario','description':'EDIÇÃO USUARIO'},
]

@roles_accepted('admin')
def novo_usuario():
    form = UserForm()
    if form.validate_on_submit():
        obj  = User()
        form.populate_obj(obj)
        db.session.add(obj)
        obj.password  = encrypt_password(obj.password)
        db.session.commit()
        flash(CADASTRADO_COM_SUCESSO.format('Usuário'), 'success')
        return redirect(url_for('core.novo_usuario'))
    return render_template('auth/form.html',form=form)

@roles_accepted('admin')
def editar_usuario(id):
    obj = User.query.filter_by(id=id).first_or_404()
    form = UserForm(obj=obj)
    senha = obj.password
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        flash(ATUALIZADO_COM_SUCESSO.format('Usuário'), 'success')
    return render_template('auth/form.html',form=form)


def reset_senha_usuario_local():
    form = UserFormResetPassword()
    if form.validate_on_submit():
        current_user.password = encrypt_password(form.password.data)
        db.session.commit()
        return render_template('auth/reset_senha.html',form=form)
    return render_template("auth/reset_senha.html", form=form)


@roles_accepted('admin')
def admin_reset_senha(id):
    obj = User.query.filter_by(id=id).first_or_404()
    form = UserFormResetPassword()
    if form.validate_on_submit():
        obj.password = encrypt_password(form.password.data)
        db.session.commit()
        return render_template('auth/reset_senha.html',form=form,obj=obj)
    return render_template("auth/reset_senha.html", form=form,obj=obj)   
    
@roles_accepted('admin')
def usuarios():
    usuarios = User.query.all()
    return render_template("auth/usuarios.html", lista=usuarios)

routes.append(dict(rule='usuarios',view_func=usuarios, options=dict(methods=['GET'])))
routes.append(dict(rule='usuario',view_func=novo_usuario, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='usuario/<int:id>',view_func=editar_usuario, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='usuario-reset-senha/',view_func=reset_senha_usuario_local, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='usuario/<int:id>/reset-senha/',view_func=admin_reset_senha, options=dict(methods=['GET','POST'])))
