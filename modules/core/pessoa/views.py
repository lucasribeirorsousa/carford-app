from ext.db import db
import requests,json
from flask_wtf import FlaskForm
from functools import wraps
from modules.core.pessoa.forms import PessoaForm
from modules.core.pessoa.models import Pessoa
from flask_security.decorators import roles_required,roles_accepted
from flask import render_template, request, jsonify,redirect,url_for,flash,g,abort ,current_app as app
from modules.core.messages import *

routes = []

@roles_accepted('admin')
def pessoas():
    return render_template("pessoa/lista.html",lista=Pessoa.query.filter())    

@roles_accepted('admin')
def pessoa_edicao(id):
    obj = Pessoa.query.filter_by(id=id).first_or_404()
    form = PessoaForm(obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        flash(ATUALIZADO_COM_SUCESSO.format('Pessoa'), 'success')  
        return redirect(url_for('core.pessoa_edicao',id=id))
    return render_template('pessoa/form.html',form=form)

@roles_accepted('admin')
def nova_pessoa():
    form = PessoaForm()
    if form.validate_on_submit():
        obj  = Pessoa()
        form.populate_obj(obj)
        db.session.add(obj)
        db.session.commit()
        flash(CADASTRADO_COM_SUCESSO.format('Pessoa'), 'success')
        return redirect(url_for('core.nova_pessoa'))
    return render_template('pessoa/form.html',form=form)

routes.append(dict(rule='pessoa',view_func=nova_pessoa, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='pessoa/<int:id>',view_func=pessoa_edicao, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='pessoas/',view_func=pessoas, options=dict(methods=['GET','POST'])))