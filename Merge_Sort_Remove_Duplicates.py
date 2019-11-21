import random
import time

# Gerando lista aleatória

lista = []

for i in range(500000):
    n = random.randint(1,10)
    if i not in lista:
        lista.append(n)

        listagem = lista


# Fazendo função de remover duplicatas


def mergeSort(array):
    if len(array) <= 1:
        return array
    else:
        left = array[:len(array)//2]
        right = array[len(array)//2:]
        return merge(mergeSort(left),mergeSort(right))


def merge(array1, array2):
    merged_array = []
    pointer1, pointer2 = 0, 0
    while pointer1 < len(array1) and pointer2 < len(array2):
        if array1[pointer1] < array2[pointer2]:
            merged_array.append(array1[pointer1])
            pointer1 += 1
        elif array1[pointer1] > array2[pointer2]:
            merged_array.append(array2[pointer2])
            pointer2 += 1
        else:
            array2.remove(array2[pointer2])
            
    while pointer1 < len(array1):
        merged_array.append(array1[pointer1])
        pointer1 += 1

    while pointer2 < len(array2):
        merged_array.append(array2[pointer2])
        pointer2 += 1

    return merged_array



# Medindo o tempo de execução

inicio = time.time()
mergeSort(listagem)
fim = time.time()
print("Com 500000 amostras", fim - inicio)

print(mergeSort(listagem))
