'''
1. Feladat
Írj egy programot, ami 4 darab három elemű [0;25] intervallumban lévő véletlen egész számokat tartalmazó listát generál, és ezeket a listákat egy 'tarolo' nevű listába helyezi. 
A program írja ki a képernyőre a 'tarolo' nevű lista tartalmát!
'''

from random import randint
tarolo = []
for i in range(4):
    lista = [randint(0,25) for szam in range(3)]
    tarolo.append(lista)

print(tarolo)