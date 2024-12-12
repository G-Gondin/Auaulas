def arqexiste(nome):
    try:
        a = open(nome, "rt")
    except FileNotFoundError:
        return False
    else:
        return True

def criararq(nome):
    a = open(nome, "wt+")
    a.close()

def cria_id():
    """Cria um ID aleatoriamente"""

    from random import randint
    id = ""
    while len(id) < 7:
        id += str(randint(1, 9))
    return id

def verify_id(arq, id):
    """Verifica se tem um determinado id dentro do arquivo selecionado
    arq = arquivo selecionado
    id = id a ser verificado"""
    
    n1 = open(arq, "rt")
    for c in n1:
        lis = c.split()
        if lis[2] == id:
            n1.close()
            return True
    else:
        n1.close()
        return False

def cadastra_users(arq, name, region, city, age):
    try:
        a = open(arq, "at")
        a.write(f"{name},{region},{city},{age}")
        a.close()
    except:
        return "Houve um erro inesperado"
    else:
        return "Pessoa cadastrada com sucesso!"

def jogalist(arq):
    a = open(arq, "rt")
    tusuarios = []
    for c in a:
        tusuarios.append(c.split(","))
    a.close()
    return tusuarios