# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request, redirect
from wtforms import StringField, PasswordField, Form, fields, SubmitField
from ..models.base import Base

site.setup(engine)


# -------------- Controle das views de concordancia
cl_login = Bottle(True)

"""
### --------------  Form Login -------------- ###
"""
class Login(Form):
    username = StringField('Username')
    password = PasswordField('Password')
    butt = SubmitField('OK!')

"""
### --------------  Login -------------- ###
"""
# -------------- Página: Cadastro
@cl_login.route('/login')
@jinja2_view('adm/login.html')
def g_login():
    return dict(title = 'Login', form = Login())

# -------------- Insere: Cadastro
@cl_login.post('/login')
def p_login():
    db = Base()
    form = Login(request.POST)   # ----- POST METHOD
    name = form.username.data
    password = form.password.data

    try:
        user = db.login(name, password)
        assert user != 0
        return redirect('/')

    except AssertionError:
        return redirect('/error_db2')
