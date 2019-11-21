# Gerando uma lista aleatória com duplicatas

import random
import time

lista = [] # Criando uma lista vazia

for i in range(1000): # para i em um intervalo de 1000 números
	n = random.randint(1,10) # criar uma lista onde cada elemento varia de 1 ate 10
	if i not in lista:
		lista.append(n)

	listagem = lista # Guardando a lista gerada em uma variável


def remove_duplicates_brute(x):
    i=0

# i percorre até o penúltimo elemento da lista
    while i < len(lista)-1:
        #j sempre vai iniciar um índice a frente de i
        j = i+1
        #j percore até o ultimo iten da lista
        while j< len(lista):
                #se a lista i = a lista j remove,
                if lista[i] == lista [j]:
                        lista.pop(j)
                #se não incrementa o proximo indice de j
                else:
                        j = j+1
        #incrementa o i
        i = i+1
    print(lista)


# Medindo tempo da função

inicio = time.time()
remove_duplicates_brute(listagem)
fim = time.time()
print("Tempo com 1000 amostras", fim - inicio)
