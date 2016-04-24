# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request, redirect
from wtforms import StringField, PasswordField, Form, fields, SubmitField
from ..models.base import Base

# -------------- Controle das views de concordancia
cl_cadastro = Bottle(True)

"""
### --------------  Form Cadastro -------------- ###
"""
class Cadastro(Form):
    username = StringField('Username')
    email = StringField('Email')
    password = PasswordField('Password')
    butt = SubmitField('OK!')

"""
### --------------  Páginas Administrativas -------------- ###
"""

# -------------- Página: Cadastro
@cl_cadastro.route('/cadastro')
@jinja2_view('adm/cadastro.html')
def cadastro():
    return dict(title = 'Cadastro', form = Cadastro())

# -------------- Insere: Cadastro
@cl_cadastro.post('/cadastro')
def cadastro():
    db = Base()
    form = Cadastro(request.POST)   # ----- POST METHOD
    name = form.username.data
    email = form.email.data
    password = form.password.data

    try:
        assert name != ''
        assert email != '' and "@" in email
        assert password != ''

        db.inserir_dados(name,email, password)
        db.commit()

        return redirect('/')

    except AssertionError:
        return redirect('/error_db')

"""
### --------------  Pagina de visualização dos dados do banco   -------------- ###
"""
@cl_cadastro.route('/base')
@jinja2_view('adm/base.html')
def base():
    try:
        db = Base()
        data = db.busca()
        assert data[0]
        return dict(rows=data)
    except:
        return redirect('/error_db1')
