import json
from ext.db import db
from flask import url_for
from flask_wtf import FlaskForm
from wtforms_alchemy import Unique,ModelForm
from wtforms.widgets import ListWidget, RadioInput,CheckboxInput
from modules.core.forms import BaseForm
from wtforms import (PasswordField, StringField, BooleanField,SubmitField, ValidationError,
    SelectField,SelectMultipleField,Form,FloatField,validators,TextAreaField,IntegerField
)
from wtforms_alchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms.fields import DateField,EmailField,URLField,IntegerRangeField,DecimalField
from modules.core.messages import *

class PessoaForm(BaseForm):
    nome = StringField('Nome',render_kw={'maxlength':'255','required':''},validators=[validators.DataRequired()])
    email = EmailField('Email',render_kw={'maxlength':'255','required':''},validators=[validators.DataRequired()])
    telefone = StringField('Telefone',render_kw={'maxlength':'255','required':''},validators=[validators.DataRequired()])
    cpf = StringField('CPF',render_kw={'maxlength':'11','required':'','type':'number'},validators=[validators.DataRequired()])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)