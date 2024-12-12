from script import *

if arqexiste("teste1") == False:
    criararq("teste1")
if arqexiste("teste2") == False:
    criararq("teste2")

n = 0
while True:
    if n % 2 == 0:
        nome = str(input("Nome: ")).strip().lower()
        senha = str(input("Senha: ")).strip()
        cadastra_users("teste1", nome, senha)
    else:
        nome = str(input("Nome: ")).strip().lower()
        senha = str(input("Senha: ")).strip()
        cadastra_users("teste2", nome, senha)
    
    

    s = str(input("Quer sair? [s/n]")).lower().strip()
    if s not in "sn" or s == "" or len(s) > 1:
        while s not in "sn" or s == "" or len(s) > 1:
            s = str(input("Erro, digite novamente: ")).strip().lower()
    if s == "s":
        break
    n += 1