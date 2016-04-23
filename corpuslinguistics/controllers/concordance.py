# -*- coding: utf-8 -*-
from bottle import Bottle, jinja2_view, post, request, redirect
from ..models.Auxiliar import Auxiliar, concord

# -------------- Controle das views de concordancia
cl_concordance = Bottle(True)

"""
### --------------  Página de concordancia   -------------- ###
"""

# -------------- Página: Concordância
@cl_concordance.route('/concordancia')
@jinja2_view('sistema/concordancia.html')
def concordancia():
    return dict(title = 'Concordância')

# -------------- Post: Concordância
@cl_concordance.post('/concordancia')
@jinja2_view('out/concord.html')
def upload_concordancia():
    auxiliar = Auxiliar()
    pasta = auxiliar.concordancia

    arquivo = request.files.get('arquivo')
    palavra = request.forms.get('palavra')

    chave = auxiliar.upload_um_arquivo(arquivo, pasta, palavra)

    # ---------- Nome do arquivo sem extensão
    _arquivo = arquivo.filename

    if chave == 0:
        return redirect("/error_0")
    elif chave == 1:
        concord(_arquivo, palavra)
        saida = open("/tmp/concordancia/saida.txt", "r")
        return dict(rows=saida, name="Concord")

    elif chave == 2:
        return redirect("/error_2")
