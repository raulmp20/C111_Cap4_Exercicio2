import numpy as np

#Exercicio 1
np.random.seed(5)
arr = np.random.randn(10)

mult = arr * 100

new_arr = np.floor(mult)
print(new_arr)

#Exercicio 2
np.random.seed(10)
matriz = np.random.randint(1, 51, size=(4, 4))

print(matriz)

#Exercicio 3
print("Media da coluna 0: ")
col0 = matriz.mean(axis=0)[0]
print(col0)

print("Media da coluna 1: ")
col1 = matriz.mean(axis=0)[1]
print(col1)

print("Media da coluna 2: ")
col2 = matriz.mean(axis=0)[2]
print(col2)

arr_colu = np.array([col0, col1, col2])

print("Media da linha 0: ")
lin0 = matriz.mean(axis=1)[0]
print(lin0)

print("Media da linha 1: ")
lin1 = matriz.mean(axis=1)[1]
print(lin1)

print("Media da linha 2: ")
lin2 = matriz.mean(axis=1)[2]
print(lin2)

arr_linha = np.array([lin0, lin1, lin2])

print("Maior media das colunas: ")
print(arr_colu.max(axis=0))

print("Maior media das linhas: ")
print(arr_linha.max(axis=0))

#Exercicio 4
valores, contagens = np.unique(matriz, return_counts=True)
aparicoes = dict(zip(valores, contagens))
print(aparicoes)

numeros_repetidos = [numero for numero, contagem in aparicoes.items() if contagem == 2]
print(numeros_repetidos)

