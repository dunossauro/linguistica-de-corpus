# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request
from ..models.base import Base

# -------------- Controle das views de concordancia
cl_db = Bottle(True)

"""
### --------------  Páginas Administrativas -------------- ###
"""

# -------------- Página: Cadastro
@cl_db.route('/cadastro')
@jinja2_view('adm/cadastro.html')
def cadastro():
    return dict(title = 'Cadastro')

# -------------- Insere: Cadastro
@cl_db.post('/cadastro')
#@jinja2_view()
def cadastro():
    db = Base()
    nome = request.forms.get('nome')
    email = request.forms.get('mail')
    try:
        assert nome != ''
        assert email != '' and "@" in email
        db.inserir_dados(nome,email)
        db.commit()
        return "ok"
    except:
        return "error"
"""
### --------------  Pagina de visualização dos dados do banco   -------------- ###
"""
@cl_db.route('/base')
@jinja2_view('adm/base.html')
def base():
    try:
        db = Base()
        data = db.busca()
        assert data[0]
        return dict(rows=data)
    except:
        return "ERROR"
