from lutv import cor
def verify(lis):
    li1 = list(lis)
    verif = ""
    pare = 0
    for num in range(0, len(li1)):
        test = str(li1[num])
        if test in verif:
            pare += 1
        else:
            verif += test
        if pare > 1:
            return int(test)
    else:
        return -1


listas = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
]

for c in range(0, len(listas)):
    liss = listas[c]
    print(liss)
    la = verify(liss)
    if la == -1:
        print(cor("nenhum número foi repetido.", "verde"))
    else:
        print(cor(f"O número repetido de segunda ocorrencia foi {la}", "vermelho"))
print("Fem")
