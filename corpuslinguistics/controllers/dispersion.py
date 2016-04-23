# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request, redirect
from ..models.Auxiliar import Auxiliar, dispersao

# -------------- Controle das views de dispersão
cl_dispersion = Bottle(True)

"""
### --------------  Página de Dispersão -------------- ###
"""

# -------------- Página: Dispersão
@cl_dispersion.route('/dispersao')
@jinja2_view('sistema/dispersao.html')
def dispersao():
    return dict(title = 'Dispersão')

# -------------- Post: Dispersão
@cl_dispersion.post('/dispersao')
@jinja2_view('out/lexical')
def upload_dispersao():
    auxiliar = Auxiliar()
    pasta = auxiliar.dispersao

    arquivo = request.files.get('arquivo')
    palavra = request.forms.get('palavra')

    chave = auxiliar.upload_um_arquivo(arquivo, pasta, palavra)

    if chave == 0:
        return redirect("/error_0")
    elif chave == 1:
        dispersao(palavra, arquivo.filename)
        saida = open("/tmp/dispersao/saida.txt", "r")
        return dict(rows=saida, name="Lexical Dispersion")
    elif chave == 2:
        return redirect("/error_2")
