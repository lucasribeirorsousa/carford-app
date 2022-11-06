from flask import Flask
from .db import db
from modules.core.auth.models import User,Role
from wtforms import StringField, BooleanField, SubmitField, validators,PasswordField
from wtforms_alchemy.fields import QuerySelectField,QuerySelectMultipleField
from wtforms.fields import EmailField
from flask_login import current_user
from flask_login import user_logged_in,user_logged_out,user_unauthorized
from flask_security.forms import LoginForm,RegisterForm
from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin
from flask_security.utils import encrypt_password,url_for_security
from wtforms.validators import DataRequired, Email, EqualTo

class ExtendedLoginForm(LoginForm):
    email = EmailField("Email ", [validators.length(min=2, max=15), validators.DataRequired()])
    password = PasswordField("Password ", [validators.DataRequired()])
    username = StringField('Usuario',validators=[DataRequired()])
    remember_me = BooleanField("Remember Me")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ExtendedRegisterForm(RegisterForm):
    active = BooleanField('Ativo')
    email = EmailField('Email',validators=[DataRequired()])
    

def context_security(app:Flask):
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    @app.context_processor
    def login_context():
        return {
            'url_for_security': url_for_security,
            'login_form': ExtendedLoginForm(),
            'register_form':ExtendedRegisterForm(),
        }

    @app.before_first_request
    def create_user():
        with app.app_context():
            db.create_all()
            if db.session.query(User).filter_by(username='master',email='master@localhost.com.br').count() == 0:
                user_datastore.create_user(username='master', email='master@localhost.com.br', password=encrypt_password('123456789'))
            db.session.commit()
            user_datastore.find_or_create_role(name='admin', description='Permissao total')
            user_datastore.add_role_to_user('master@localhost.com.br','admin')
            db.session.commit()
            
            
                