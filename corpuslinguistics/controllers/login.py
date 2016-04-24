# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request
from wtforms import StringField, PasswordField, Form, fields, SubmitField
from ..models.base import Base
from hashlib import sha512

# -------------- Controle das views de concordancia
cl_login = Bottle(True)

"""
### --------------  Form Login -------------- ###
"""
class Cadastro(Form):
    username = StringField('Username')
    password = PasswordField('Password')
    butt = SubmitField('OK!')
