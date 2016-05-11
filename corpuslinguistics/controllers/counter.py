# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request, redirect
from ..models.Auxiliar import Auxiliar, contagem
from ..models.graficos import Grap

# -------------- Controle das views de contagem
cl_counter = Bottle(True)

"""
### --------------  Página do Contador   -------------- ###
"""

# -------------- Página: Contador
@cl_counter.route('/contador')
@jinja2_view('sistema/contador.html')
def contador(upload=''):
    return dict(title = 'Contador',
                upload = upload)

# -------------- Post: Contador
@cl_counter.post('/contador')
@jinja2_view('out/counter')
def upload_contador():
    auxiliar = Auxiliar()
    pasta = auxiliar.contador

    arquivo = request.files.get('arquivo')

    chave = auxiliar.upload_um_arquivo(arquivo, pasta)

    if chave == 0:
        return redirect("/error_0")
    elif chave == 1:
        saida = contagem(arquivo.filename)
        return dict(rows=saida, name="Word Counter")
    elif chave == 2:
        return redirect("/error_2")
