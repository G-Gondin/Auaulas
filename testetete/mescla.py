from script import *

if arqexiste("teste1.txt") == False:
    criararq("teste1.txt")
if arqexiste("teste2.txt") == False:
    criararq("teste2.txt")
if arqexiste("final.txt") == False:
    criararq("final.txt")

n1 = jogalist("teste1.txt")
n2 = jogalist("teste2.txt")

if len(n1) > len(n2):
    b = 0
    for c in range(0, len(n1)):
        for d in range(0, len(n2)):
            if n1[c] == n2[d]:
                n2.remove(n1[c])
                b = 1
                break
        if b == 1:
            b = 0
            continue

if len(n2) > len(n1):
    b = 0
    for c in range(0, len(n2)):
        for d in range(0, len(n2)):
            if n2[c] == n1[d]:
                n1.remove(n2[c])
                b = 1
                break
        if b == 1:
            b = 0
            continue

if len(n1) == len(n2):
    b = 0
    for c in range(0, len(n1)):
        for d in range(0, len(n2)):
            if n1[c] == n2[d]:
                n2.remove(n1[c])
                b = 1
                break
        if b == 1:
            b = 0
            continue


for c in range(0, len(n2)):
    n1.append(n2[c])

a = open("final.txt", "wt")
for c in range(0, len(n1)):
    cadastra_users("final.txt", n1[c][0], n1[c][1], n1[c][2])
a.close()

print("Fim")
