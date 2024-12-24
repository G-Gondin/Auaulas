from random import randint

cartas = [
["a", "ouros"], ["2", "ouros"], ["3", "ouros"], ["4", "ouros"], ["5", "ouros"], ["6", "ouros"], ["7", "ouros"], ["8", "ouros"], ["9", "ouros"], ["10", "ouros"], ["J", "ouros"], ["Q", "ouros"], ["K", "ouros"],
["a", "espadas"], ["2", "espadas"], ["3", "espadas"], ["4", "espadas"], ["5", "espadas"], ["6", "espadas"], ["7", "espadas"], ["8", "espadas"], ["9", "espadas"], ["10", "espadas"], ["J", "espadas"], ["Q", "espadas"], ["K", "espadas"],
["a", "copas"], ["2", "copas"], ["3", "copas"], ["4", "copas"], ["5", "copas"], ["6", "copas"], ["7", "copas"], ["8", "copas"], ["9", "copas"], ["10", "copas"], ["J", "copas"], ["Q", "copas"], ["K", "copas"],
["a", "paus"], ["2", "paus"], ["3", "paus"], ["4", "paus"], ["5", "paus"], ["6", "paus"], ["7", "paus"], ["8", "paus"], ["9", "paus"], ["10", "paus"], ["J", "paus"], ["Q", "paus"], ["K", "paus"]]

baralho = cartas.copy()
jogador1 = []
jogador2 = []
jogador3 = []
jogador4 = []
comunitaria = []
for c in range(0, 2):
    carta = cartas[randint(0, len(baralho))]
    jogador1.append(carta)
    baralho.remove(carta)

    carta = cartas[randint(0, len(baralho))]
    jogador2.append(carta)
    baralho.remove(carta)

    carta = cartas[randint(0, len(baralho))]
    jogador3.append(carta)
    baralho.remove(carta)

    carta = cartas[randint(0, len(baralho))]
    jogador4.append(carta)
    baralho.remove(carta)


carta = cartas[randint(0, len(baralho))]
baralho.remove(carta)

carta = cartas[randint(0, len(baralho))]
comunitaria.append(carta)

carta = cartas[randint(0, len(baralho))]
comunitaria.append(carta)

carta = cartas[randint(0, len(baralho))]
comunitaria.append(carta)

carta = cartas[randint(0, len(baralho))]
baralho.remove(carta)

carta = cartas[randint(0, len(baralho))]
comunitaria.append(carta)

carta = cartas[randint(0, len(baralho))]
baralho.remove(carta)

carta = cartas[randint(0, len(baralho))]
comunitaria.append(carta)

print(f"""jogador 1: {jogador1[0]} {jogador1[1]}
jogador 2: {jogador2[0]} {jogador2[1]}
jogador 3: {jogador3[0]} {jogador3[1]}
jogador 4: {jogador4[0]} {jogador4[1]}
comunitaria: {comunitaria[0]} {comunitaria[1]} {comunitaria[2]} {comunitaria[3]} {comunitaria[4]}""")
