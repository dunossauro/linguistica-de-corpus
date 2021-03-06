from bottle import Bottle, jinja2_view, post, request, redirect, error

# -------------- Controle das views de erro
cl_error = Bottle(True)

"""
### --------------  Página de Erro   -------------- ###
"""

# -------------- Página: Erro_0 - Arquivo em outro formato
@cl_error.route('/error_0')
@jinja2_view('out/error.html')
def error_0():
    return dict(out="Utilize apenas arquivos .txt e com encode utf-8", title="Upload Error")

# -------------- Página: Erro_2 - Arquvi já está no sistema
@cl_error.route('/error_2')
@jinja2_view('out/error.html')
def error_2():
    return dict(out="Um arquivo com esse nome já existe no sistema", title="Upload Error")

# -------------- Página: Erro_db - Cadastro sem assert
@cl_error.route('/error_db')
@jinja2_view('out/error.html')
def error_2():
    return dict(out="Cadastro não efetuado", title="Error")

# -------------- Página: Erro_db1 - Banco indisponível
@cl_error.route('/error_db1')
@jinja2_view('out/error.html')
def error_2():
    return dict(out="Algo aconteceu com a sua base de dados, tente novamente", title="Error")

# -------------- Página: Erro_db2 - Usuário não cadastrado
@cl_error.route('/error_db2')
@jinja2_view('out/error.html')
def error_2():
    return dict(out="Você não está cadastrado no sistema", title="Error")
