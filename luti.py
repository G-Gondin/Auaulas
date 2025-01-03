def identmao1(jogad):
    n = []
    n = jogad.copy()
    print(n)
    if n[0][0] == n[1][0]:
        mao = "par"
    else:
        mao = "carta alta"
    return mao

def jogalis(jogad, comu):
    ls = []
    for c in range(0, 2):
        ls.append(jogad[c])
    for c in range(0, 5):
        ls.append(comu[c])
    return ls




def ispar(cards):
    ls = cards
    a = []
    repetidos = ""
    for c in range(0, len(ls)):
        a.append(ls[c][0])
    for c in range(0, len(a)):
        if a.count(a[c]) > 1:
            if a[c] not in repetidos:
                repetidos += a[c]
    if len(repetidos) == 1:
        return True
    else:
        return False

def is2par(cards):
    ls = cards
    a = []
    repetidos = ""
    for c in range(0, len(ls)):
        a.append(ls[c][0])
    for c in range(0, len(a)):
        if a.count(a[c]) > 1:
            if a[c] not in repetidos:
                repetidos += a[c]
    if len(repetidos) == 2:
        return True
    else:
        return False

def istrinca(cards):
    ls = cards
    a = []
    repetidos = ""
    for c in range(0, len(ls)):
        a.append(ls[c][0])
    for c in range(0, len(a)):
        if a.count(a[c]) > 1:
            if a[c] not in repetidos:
                quant = a.count(a[c])
                repetidos += a[c]
    rept = []
    rept.append(repetidos)
    if quant == 3 and len(rept) == 1:
        return True
    else:
        return False

def istrai(cards):
    ...
def isflush(cards):
    ls = cards
    a = []
    for c in range(0, len(ls)):
        a.append(ls[c][1])
    for c in range(0, len(a)):
        if a.count(a[c]) == 5:
            return True
    else:
        return False

def isfull(cards):
    ...
def isquadra(cards):
    ls = cards
    a = []
    for c in range(0, len(ls)):
        a.append(ls[c][0])
    for c in range(0, len(a)):
        if a.count(a[c]) == 4:
            return True
    else:
        return False
    
def istraiflush(cards):
    ...
def isroyal(cards):
    ...


def identmao(jogad, comu):
    ls = jogalis(jogad, comu)

    if ispar(ls) == True:
        mao = "Par"
    if is2par(ls) == True:
        mao = "Dois Pares"
    if istrinca(ls) == True:
        mao = "Trinca"
    if istrai(ls) == True:
        mao = "Straight"
    if isflush(ls) == True:
        mao = "Flush"
    if isfull(ls) == True:
        mao = "Full House"
    if isquadra(ls) == True:
        mao = "Quadra"
    if istraiflush(ls) == True:
        mao = "Straight Flush"
    if isroyal(ls) == True:
        mao = "Royal Flush"    
    else:
        mao = "Carta Alta"
    return mao