'''
Função que le um vetor V com 20 posições e substitui 
todos os valores nulos e negativos do vetor V por 1, 
em seguida retorna o vetor alterado.
'''
import random as rd

def Sub(L1):
    for pos in range(len(L1)):
        if L1[pos] <= 0:
            L1[pos] = 1
    return L1

V = []
for i in range(20):
    V.append(rd.randint(-100,100))

print(V)
print(Sub(V))

'''
Função que percorre uma matriz(MAT) e retorna a posição de um número inteiro(n). 
'''
def posicao(MAT,n):
    Lpos = []
    print(MAT)
    rng = len(MAT)
    for i in range(rng):
        for j in range(len(MAT[i])):
            if MAT[i][j] == n:
                Lpos.append((i,j))
    return Lpos

matriz = [[5,6,4],[3,5,8],[1,4,5]]
num = 5

print(matriz)
print('Posição de num: \n 'posicao(matriz,num))

'''
Função que verifica se a frase é ou não um tautograma!
'''
def tautogram(string):
    string_separada = string.split(' ')
    if len(string_separada)>50:
        print("A frase deve possuir até 50 palavras.")
        exit()
    for letra in string_separada:
        if letra[0].upper() != string[0].upper():
            print(string)
            return "N"

    print(string)       
    return "Y"

frase = 'This is NOT a tautogram'
print(tautogram(frase))

'''
Função que retorna a soma dos elementos de 2 matrizes.
'''
def somamatriz(M1):
    s = 0
    nlinhas = len(M1)
    ncolunas = len(M1[0])

    for linha in range(nlinhas):
        for coluna in range(ncolunas):
            s = s+M1[linha][coluna]
        return s

v = [[1,2,3],[4,5,6],[7,8,9]]

print(somamatriz(v))
