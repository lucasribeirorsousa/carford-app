import json
from ext.db import db
from flask import url_for
from flask_wtf import FlaskForm
from wtforms_alchemy import Unique,ModelForm
from wtforms.widgets import ListWidget, RadioInput,CheckboxInput
from modules.core.veiculos.choices import modelos,cores
from modules.core.pessoa.models import Pessoa
from modules.core.forms import BaseForm
from wtforms import (PasswordField, StringField, BooleanField,SubmitField, ValidationError,
    SelectField,SelectMultipleField,Form,FloatField,validators,TextAreaField,IntegerField
)
from wtforms_alchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms.fields import DateField,EmailField,URLField,IntegerRangeField,DecimalField
from modules.core.messages import *

class VeiculoForm(BaseForm):
    pessoa = QuerySelectField(label=u"Cliente", get_pk=lambda x: x.id,query_factory=lambda: \
        db.session.query(Pessoa).filter().order_by(Pessoa.nome.asc()),
        get_label=lambda item: "{0}".format(item.nome),
        allow_blank=True,validators = [validators.DataRequired()]
    )
    placa = StringField('Placa',render_kw={'maxlength':'10','required':''},validators=[validators.DataRequired()])
    modelo = SelectField('Modelo', coerce=str, choices=modelos, validators=[validators.DataRequired()])
    cor = SelectField('Modelo', coerce=str, choices=cores, validators=[validators.DataRequired()])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def validate_pessoa(form, field):
        if len(field.data.veiculo_pessoa) >= 3:
            raise validators.ValidationError("QUANTIDADE DE VEICULOS EXCEDIDOS")

class VeiculoEditForm(BaseForm):
    pessoa = QuerySelectField(label=u"Cliente", get_pk=lambda x: x.id,query_factory=lambda: \
        db.session.query(Pessoa).filter().order_by(Pessoa.nome.asc()),
        get_label=lambda item: "{0}".format(item.nome),
        allow_blank=True,validators = [validators.DataRequired()]
    )
    placa = StringField('Placa',render_kw={'maxlength':'10','required':''},validators=[validators.DataRequired()])
    modelo = SelectField('Modelo', coerce=str, choices=modelos, validators=[validators.DataRequired()])
    cor = SelectField('Modelo', coerce=str, choices=cores, validators=[validators.DataRequired()])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        



