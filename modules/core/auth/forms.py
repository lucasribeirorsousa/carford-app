from dataclasses import dataclass
import json
from ext.db import db
from flask_wtf import FlaskForm
from wtforms_alchemy import Unique,ModelForm
from modules.core.auth.models import User,Role
from modules.core.forms import BaseForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError,SelectField,Form,FloatField,validators
from wtforms_alchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms import DecimalField, RadioField ,FileField,FieldList,FormField,SelectMultipleField, BooleanField,StringField,PasswordField, validators,SelectField,IntegerField,RadioField,HiddenField,TextAreaField
from wtforms.fields import DateField,EmailField,URLField,IntegerRangeField
from flask_security.forms import LoginForm,RegisterForm,ChangePasswordForm
from modules.core.messages import *
from decimal import *

class UserForm(BaseForm,ModelForm):
    username = StringField('Usuario',validators=[validators.DataRequired(),Unique(User.username,message=ITEM_JA_CADASTRADO.format('Usuário'))] , render_kw={'maxlength':'255'})
    active = BooleanField('Ativo',default = False)
    email = EmailField('Email',validators=[validators.DataRequired(),Unique(User.email,message=ITEM_JA_CADASTRADO.format('Email'))])
    email_confirmacao = EmailField('Email Confirmação',validators = [validators.EqualTo('email', message='Emails não são os mesmos')])
    nome_completo = StringField('Nome Completo',validators=[validators.DataRequired()])
    roles = QuerySelectMultipleField( 
        label=u"Permissões", get_pk=lambda x: x.id, 
        query_factory=lambda: Role.query,
        get_label=lambda item: item.description.upper() ,
        render_kw={'select2':''} 
    )


class UserFormResetPassword(BaseForm):
    password = PasswordField('Senha',validators=[validators.DataRequired()])
    confirmacao_senha = PasswordField('Confirmacao senha',validators=[validators.DataRequired(),validators.EqualTo('password',message='Senha não são as mesmas')])
    
