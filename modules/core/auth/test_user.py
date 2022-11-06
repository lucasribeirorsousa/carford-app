import sys
from flask import url_for
from ext.db import db 
from flask_login import login_user
from flask_security.utils import login_user,hash_password,verify_password,encrypt_password
from modules.core.auth.models import User,Role
from modules.core.messages import *

def test_userviews(create_user,client,captured_templates):
    resp = client.get(url_for('core.novo_usuario'),follow_redirects=True)
    template, context = captured_templates[0]
    assert resp.status_code == 200
    assert template.name == "auth/form.html"
    data = dict( username="teste_002", active = True,
        envio_ilimitado=False,email='t@gmail.com',
        email_confirmacao='t@gmail.com',
        nome_completo = 'TESTE 002 CONTA 001',
        celular='000000',rg='00000000',
        cpf_cnpj='0000000000'
    )
    resp = client.post(url_for('core.novo_usuario'), data=data, follow_redirects=True)
    template, context = captured_templates[0]
    assert template.name == "auth/form.html"
    assert resp.status_code == 200
    user = User.query.filter(User.username==data['username']).first()
    resp = client.post(url_for('core.editar_usuario',id=user.id), data=data, follow_redirects=True)
    template, context = captured_templates[0]
    assert template.name == "auth/form.html"
    assert resp.status_code == 200
    assert User.query.count() == 3

def test_list_users(create_user,client,captured_templates):
    resp = client.get(url_for('core.usuarios'),follow_redirects=True)
    template, context = captured_templates[0]
    assert resp.status_code == 200
    assert template.name == "auth/usuarios.html"

def test_reset_senha(create_user,client,captured_templates):
    user = User.query.filter_by(username='teste').first()
    resp = client.get(url_for('core.reset_senha_usuario_local'),follow_redirects=True)
    template, context = captured_templates[0]
    assert resp.status_code == 200
    assert template.name == "auth/reset_senha.html"

    data = dict( password="001", confirmacao_senha = '001')
    resp = client.post(url_for('core.reset_senha_usuario_local'),data =data, follow_redirects=True)
    template, context = captured_templates[0]
    assert verify_password(data['password'],user.password)
    assert resp.status_code == 200


def test_user_reset_senha_admin(create_user,client,captured_templates):
    user = User.query.filter_by(username='teste').first()
    resp = client.get(url_for('core.admin_reset_senha',id=user.id), follow_redirects=True)
    template, context = captured_templates[0]
    assert template.name == "auth/reset_senha.html"
    assert resp.status_code == 200

    data = dict( password="002", confirmacao_senha = '002')
    resp = client.post(url_for('core.admin_reset_senha',id=user.id),data =data, follow_redirects=True)
    template, context = captured_templates[0]
    assert verify_password(data['password'],user.password)
    assert resp.status_code == 200
    assert template.name == "auth/reset_senha.html"