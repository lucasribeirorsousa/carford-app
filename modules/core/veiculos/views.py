from ext.db import db
import requests,json
from flask_wtf import FlaskForm
from functools import wraps
from modules.core.veiculos.forms import VeiculoForm, VeiculoEditForm
from modules.core.veiculos.models import Veiculos
from flask_security.decorators import roles_required,roles_accepted
from flask import render_template, request, jsonify,redirect,url_for,flash,g,abort ,current_app as app
from modules.core.messages import *

routes = []

@roles_accepted('admin')
def veiculos():
    return render_template("veiculo/lista.html",lista=Veiculos.query.filter())    

@roles_accepted('admin')
def veiculo_edicao(id):
    obj = Veiculos.query.filter_by(id=id).first_or_404()
    form = VeiculoEditForm(obj=obj)
    if form.validate_on_submit():
        form.populate_obj(obj)
        db.session.commit()
        flash(ATUALIZADO_COM_SUCESSO.format('Veiculo'), 'success')  
        return redirect(url_for('core.veiculo_edicao',id=id))
    return render_template('veiculo/form.html',form=form)


@roles_accepted('admin')
def novo_veiculo():
    form = VeiculoForm()
    if form.validate_on_submit():
        obj  = Veiculos()
        form.populate_obj(obj)
        db.session.add(obj)
        db.session.commit()
        flash(CADASTRADO_COM_SUCESSO.format('Veiculo'), 'success')
        return redirect(url_for('core.novo_veiculo'))
    return render_template('veiculo/form.html',form=form)

routes.append(dict(rule='veiculo',view_func=novo_veiculo, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='veiculo/<int:id>',view_func=veiculo_edicao, options=dict(methods=['GET','POST'])))
routes.append(dict(rule='veiculos/',view_func=veiculos, options=dict(methods=['GET','POST'])))