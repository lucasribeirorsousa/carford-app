import pytest
from flask import Flask,template_rendered,url_for
from factory import create_app
from flask_security.utils import login_user,hash_password,verify_password
from modules.core.auth.models import User,Role
from ext.db import db 
from ext.config import config
from sqlalchemy import event
from flask_login import user_logged_in,user_logged_out,user_unauthorized,logout_user,login_user
from sqlalchemy.orm import sessionmaker

@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)



@pytest.fixture
def create_user(client):
    pwd = hash_password('11')
    user  = User(**{ 'active':True,'username':'teste','email':'teste@teste.com.br','password':pwd})
    role = Role(**{'name':'admin','description':'admin'})
    db.session.add(user)
    db.session.commit()
    db.session.add(role)
    user.roles.append(role)
    db.session.commit()
    data = dict(email=user.username, password='11')
    response = client.post(
        '/login?next=/',
        data=data,
        follow_redirects=True)
    return user

@pytest.fixture
def app():
    return create_app("test")

