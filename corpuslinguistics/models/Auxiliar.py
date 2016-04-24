from nltk import Text, FreqDist, word_tokenize, ConcordanceIndex
from re import compile
from collections import Counter
from os import path, makedirs, remove

regex = compile("\w+")

# -------------- Classe para auxiliar elementos ou páginas do Bottle
class Auxiliar:
    def __init__(self):
        self.nome = 'Linguística de Corpus'

        # -------------- E-mail para alteração em todo o sistema
        self.email_0 = 'diego.valls13@yahoo.com.br'
        self.email_1 = 'balthazarbruna@gmail.com'
        self.email_2 = 'mendesxeduardo@gmail.com'

        # -------------- Nomes para criação de pastas
        self.concordancia = 'concordancia'
        self.contador = 'contador'
        self.dispersao = 'dispersao'
        self.comparacao = 'comparacao'

        # -------------- Chaves de retorno dos arquivos
        self.zero   = 0   #Erro de tipo de arquivo
        self.um     = 1   #Upload efetuado com sucesso
        self.dois   = 2   #Arquivo existente


    def upload_um_arquivo(self, arquivo, pasta, palavra=None):
        """ Este método faz uso dos métodos cria_palavra e cria_pasta
        Para encaminhar os arquivos que foram feitos upload no Bootle
        Para pasta /tmp """

        name, ext = path.splitext(arquivo.filename)
        if ext not in ('.txt'):
            return self.zero

        save_path = self.cria_pasta(pasta)

        if palavra:
            self.cria_palavra(palavra, save_path)

        file_path = "{path}/{file}".format(path=save_path, file=arquivo.filename)

        try:
            arquivo.save(file_path)
            return self.um
        except OSError:
            return self.dois

    def cria_palavra(self, palavra, pasta):
        """ Metodo que cria palavra a ser buscada nos arquivos chamados Pelo
        upload_um_arquivo """

        local = "{pasta}/{arquivo}".format(pasta=pasta, arquivo=palavra)
        arquivo = open(local, "w")
        arquivo.close()

    def cria_pasta(self, pasta):
        """Método que cria uma pasta com o nome da aplicação referente ao
        processamento de Lingua """

        save_path = "/tmp/{pasta}".format(pasta=pasta)
        if not path.exists(save_path):
            makedirs(save_path)

        return save_path

def file_remove(dir,arquivo):
    """
    Remove o arquivo que foi feito upload pelo usuário
    """
    remove("/tmp/{dir}/{arquivo}".format(dir=dir,arquivo=arquivo))

def compare(arquivo_0, arquivo_1):
    """
    ??????
    """

    wl1 = arquivo_0
    wl2 = arquivo_1

    #print(wl1, wl2)

    arq_1 = open("/tmp/comparacao/{arquivo}".format(arquivo=wl1))
    arq_2 = open("/tmp/comparacao/{arquivo}".format(arquivo=wl2))

    D1 = {}
    for x in arq_1:
        num, word = x.split()
        D1[word] = num

    D2 = {}
    for x in arq_2:
        num, word = x.split()
        D2[word] = num

    arquivo_s = open("/tmp/comparacao/saida.txt","w")
    for x in sorted(D1):
        for y in D2:
            if x == y:
                arquivo_s.write(("%s\t%s\t%s\t%s\n")%(D1[x],x,y,D2[y]))

    arquivo_s.close()
    arq_1.close()
    arq_2.close()

    #Remove os arquivos do upload
    file_remove("comparacao",wl1)
    file_remove("comparacao",wl2)

def contagem(_arquivo):
    arquivo = _arquivo

    # Abertura do aquivo a ser lido
    arquivo_e = open("/tmp/contador/{arquivo}".format(arquivo=arquivo)).read()
    # Abertura do arquivo de saida
    arquivo_s = open("/tmp/contador/saida.txt","w")

    # tokenização do arquivo
    token = Counter(arquivo_e.split())

    for x in sorted(token):
        arquivo_s.write("%s\t\t%s\n" % (x, token[x]))

    arquivo_s.close()

    #Remove o arquivo do upload
    file_remove("contador",arquivo)

# Base to function: https://simplypython.wordpress.com/2014/03/14/saving-output-of-nltk-text-concordance/
def concordance_2_txt(nome_p, tokens, left_margin=2, right_margin=4):
    text = Text(tokens)
    c = ConcordanceIndex(text.tokens)

    concordance_txt = (
    [text.tokens[list(map(lambda x: x - 5 if (x - left_margin) > 0 else 0, [offset]))[0]:offset + right_margin]
     for offset in c.offsets(nome_p)])

    return [''.join([x + ' ' for x in con_sub]) for con_sub in concordance_txt]

def concord(nome, arquivo):
    """
    ??????
    """
    # Entrada
    nome_p = arquivo
    nome_e = str(nome)
    #print(nome_e,nome_p) #Para bugs

    # Abertura do aquivo a ser lido
    arquivo_e = open("/tmp/concordancia/{arquivo}".format(arquivo=nome_e)).read()

    # tokenização do arquivo
    token = word_tokenize(arquivo_e)

    texto = Text(token)

    #texto.concordance(nome_p)

    # Abertura do arquivo de saida
    arquivo_s = open("/tmp/concordancia/saida.txt","w")

    saida = concordance_2_txt(nome_p, token)

    for x in saida:
        arquivo_s.write(("%s\n") % (x))

    arquivo_s.close()

    #Remove o arquivo do upload
    file_remove("concordancia",nome_e)

def dispersao(palavra, arquivo):
    """
    Essa função recebe um arquivo e uma palavra,
    Itera sobre eles com a regex procurando somente as frases onde a palavra existe e
    Retorna um novo arquivo de texto com a dispersão das palavras seguintes as procurada

    Ex:

    Palavra = os
    Frase = "Os meninos jogam bola"

    saida: Os meninos 100%
    """

    arq = open("/tmp/dispersao/{arquivo}".format(arquivo=arquivo)) #Abertura do arquivo

    palavra = palavra
    num = 1
    list_tuple = [] #Recebe as tuplas (<Palavra>, <Proxima_palavra>)

    for x in arq:
        x = regex.findall(x)
        if  palavra in x:
            index = x.index(palavra)
            try:
                list_tuple.append(("%s %s")%(x[index],x[index+num]))
            except:
                #Insere ponto na tupla para qualquer palavra no fim da frase
                list_tuple.append(("%s %s")%(x[index],"."))

    saida = Counter(list_tuple)         #Retorna uma dicionário de contagem
    count = len(list_tuple)
    del(list_tuple)                     #Libera memória caso existam muitas tuplas

    # Abertura do arquivo de saida e escrita do arquivo de saida
    arquivo_s = open("/tmp/dispersao/saida.txt","w")
    for e in sorted(saida.keys()):
        arquivo_s.write("{chave} \t \t {valor}%\n".format(chave=e,valor=saida[e]/count*100))
    arquivo_s.close()

    #Remove o arquivo do upload
    file_remove("dispersao",arquivo)
