from luti import *
jogador1 = [["8","❤"], ["2","♦️"]] #carta alta
jogador2 = [["6","♣"], ["6","❤"]] #1par
jogador3 = [["a","♦️"], ["4","♠️"]] #2pares
jogador4 = [["10","♣"], ["10","♦️"]] #trinca
jogador5 = [["7","♣"], ["K","♠️"]] #straight
jogador6 = [["K","❤"], ["7","❤"]] #flush
comunitaria = [["10","♠️"], ["10","❤"], ["a", "❤"], ["4", "❤"], ["Q","♣"]]

ls = jogalis(jogador4, comunitaria)
print(isquadra(ls))
