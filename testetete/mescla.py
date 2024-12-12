from script import *


if arqexiste("final_file.csv") == False:
    criararq("final_file.csv")
if arqexiste("copiados.csv") == False:
    criararq("copiados.csv")

n1 = jogalist("file1.csv")
n2 = jogalist("file2.csv")
n3 = []

if len(n1) > len(n2):
    b = 0
    for c in range(0, len(n1)):
        for d in range(0, len(n2)):
            if n1[c] == n2[d]:
                n3.append(n1[c])
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
                n3.append(n1[c])
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
                n3.append(n1[c])
                n2.remove(n1[c])
                b = 1
                break
        if b == 1:
            b = 0
            continue


for c in range(0, len(n2)):
    n1.append(n2[c])

a = open("final_file.csv", "wt")
for c in range(0, len(n1)):
    cadastra_users("final_file.csv", n1[c][0], n1[c][1], n1[c][2], n1[c][3])
a.close()

a = open("copiados.csv", "wt")
for c in range(0, len(n3)):
    cadastra_users("copiados.csv", n1[c][0], n1[c][1], n1[c][2], n1[c][3])
a.close()


print("Fim")
