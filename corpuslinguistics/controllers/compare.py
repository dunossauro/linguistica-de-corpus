# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request
from ..models.Auxiliar import Auxiliar, compare

# -------------- Controle das views de comparação
cl_compare = Bottle(True)

"""
### --------------  Página de Comparação -------------- ###
"""

# -------------- Página: Comparação
@cl_compare.route('/compare')
@jinja2_view('sistema/comparacao.html')
def comparacao():
    return dict(title = 'Comparação')


# -------------- Post: Comparação
@cl_compare.post('/comparacao')
@jinja2_view('out/compare.html')
def upload_conparacao():
    auxiliar = Auxiliar()
    pasta = auxiliar.comparacao

    arquivo_0 = request.files.get('arquivo_0')
    arquivo_1 = request.files.get('arquivo_1')

    chave_0 = auxiliar.upload_um_arquivo(arquivo_0, pasta)
    chave_1 = auxiliar.upload_um_arquivo(arquivo_1, pasta)


    if chave_0 and chave_1 == 0:
        return redirect("/error_0")

    elif chave_0 and chave_1 == 1:

        compare(arquivo_0.filename,arquivo_1.filename)
        saida = open("/tmp/comparacao/saida.txt", "r")
        return dict(rows=saida, name="Compare")

    elif chave_0 and chave_1 == 2:
        return redirect("/error_2")
