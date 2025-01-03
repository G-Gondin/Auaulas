from random import shuffle

cartas = [
["a", "♦️"], ["2","♦️"], ["3", "♦️"], ["4", "♦️"], ["5","♦️"], ["6","♦️"], ["7","♦️"], ["8","♦️"], ["9","♦️"], ["10","♦️"], ["J","♦️"], ["Q","♦️"], ["K","♦️"],
["a", "♠️"], ["2","♠️"], ["3", "♠️"], ["4", "♠️"], ["5","♠️"], ["6","♠️"], ["7","♠️"], ["8","♠️"], ["9","♠️"], ["10","♠️"], ["J","♠️"], ["Q","♠️"], ["K","♠️"],
["a", "❤"], ["2","❤"], ["3", "❤"], ["4", "❤"], ["5","❤"], ["6","❤"], ["7","❤"], ["8","❤"], ["9","❤"], ["10","❤"], ["J","❤"], ["Q","❤"], ["K","❤"],
["a", "♣"], ["2","♣"], ["3", "♣"], ["4", "♣"], ["5","♣"], ["6","♣"], ["7","♣"], ["8","♣"], ["9","♣"], ["10","♣"], ["J","♣"], ["Q","♣"], ["K","♣"]]

shuffle(cartas)
shuffle(cartas)

jogador1 = []
jogador2 = []
jogador3 = []
jogador4 = []
comunitaria = []


for c in range(0,2):
    jogador1.append(cartas[0])
    cartas.remove(cartas[0])    
    jogador2.append(cartas[0])
    cartas.remove(cartas[0])
    jogador3.append(cartas[0])
    cartas.remove(cartas[0])
    jogador4.append(cartas[0])
    cartas.remove(cartas[0])

print(jogador1)
print(jogador2)
print(jogador3)
print(jogador4)

def identmao1(jogad):
    n = []
    n = jogad.copy()
    print(n)
    if n[0][0] == n[1][0]:
        mao = "par"
    else:
        mao = "carta alta"
    return mao

print(identmao1(jogador1))
print(identmao1(jogador2))
print(identmao1(jogador3))
print(identmao1(jogador4))

def identmao(jogad, comu):
    if ...:
        mao = "Par"
    elif ...:
        mao = "Dois Pares"
    elif ...:
        mao = "Trinca"
    elif ...:
        mao = "Straight"
    elif ...:
        mao = "Flush"
    elif ...:
        mao = "Full House"
    elif ...:
        mao = "Quadra"
    elif ...:
        mao = "Straight Flush"
    elif ...:
        mao = "Royal Flush"    
    else:
        mao = "Carta Alta"
    return mao

cartas.remove(cartas[0])
comunitaria.append(cartas[0])
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
cartas.remove(cartas[0])
comunitaria.append(cartas[0])
cartas.remove(cartas[0])
print(comunitaria)
print("jogador1 ",identmao(jogador1, comunitaria))
print("jogador2 ",identmao(jogador2, comunitaria))
print("jogador3 ",identmao(jogador3, comunitaria))
print("jogador4 ",identmao(jogador4, comunitaria))

cartas.remove(cartas[0])
comunitaria.append(cartas[0])
cartas.remove(cartas[0])
print(comunitaria)
print("jogador1 ",identmao(jogador1, comunitaria))
print("jogador2 ",identmao(jogador2, comunitaria))
print("jogador3 ",identmao(jogador3, comunitaria))
print("jogador4 ",identmao(jogador4, comunitaria))


cartas.remove(cartas[0])
comunitaria.append(cartas[0])
print(comunitaria)
print("jogador1 ",identmao(jogador1, comunitaria))
print("jogador2 ",identmao(jogador2, comunitaria))
print("jogador3 ",identmao(jogador3, comunitaria))
print("jogador4 ",identmao(jogador4, comunitaria))

