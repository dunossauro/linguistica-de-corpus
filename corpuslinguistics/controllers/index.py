# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view
from ..models.Auxiliar import Auxiliar

# -------------- Controle das views sem POST
cl_basic = Bottle(8080,True)


"""
### --------------  Guias da página principal    -------------- ###
"""

# -------------- Guia: Pagina principal
@cl_basic.route('/')
@jinja2_view('index.html')
def index():
    auxiliar = Auxiliar()
    return dict(title = auxiliar.nome)

# -------------- Guia: Desenvolvedores
@cl_basic.route('/jovs')
@jinja2_view('jovs.html')
def jovs():
    auxiliar = Auxiliar()
    return dict(title = auxiliar.nome,
                email_0 = auxiliar.email_0,
                email_1 = auxiliar.email_1,
                email_2 = auxiliar.email_2)

# -------------- Guia: Sobre
@cl_basic.route('/sobre')
@jinja2_view('sobre.html')
def sobre():
    return dict(title = 'Sobre')

# -------------- Guia: Ajuda
@cl_basic.route('/ajuda')
@jinja2_view('ajuda.html')
def ajuda():
    auxiliar = Auxiliar()
    return dict(title = 'Ajuda',
                email_0 = auxiliar.email_0,
                email_1 = auxiliar.email_1,
                email_2 = auxiliar.email_2)
