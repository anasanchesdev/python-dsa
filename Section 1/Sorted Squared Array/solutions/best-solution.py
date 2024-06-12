"""
S, T = O(n)
TWO POINTERS TECHNIQUE (técnica dos dois ponteiros)
- Ponteiros são números que indicam duas posições distintas de uma lista
- Neste algoritmo, "first" é o primeiro elemento da lista, inicializado como 0, e "last" é o último elemento da
lista, inicializado como a última posição da lista
- É inicializada uma lista de elementos nulos que assume o mesmo tamanho da lista original, com o intuito de servir
como base para os elementos ao quadrado conforme as devidas comparações
[...]
"""


def sortedSquared(array):
    if not array:
        return array
    length = len(array)
    new_array = [0] * length  # lista nula inicializada com o mesmo tamanho da lista original
    first, last = 0, length - 1   # criação
    for index in reversed(range(length)):
        if array[first] ** 2 > array[last] ** 2:
            new_array[index] = array[first] ** 2
            first += 1
        elif array[last] ** 2 > array[first] ** 2:
            new_array[index] = array[last] ** 2
            last -= 1
    return new_array


test_cases = (
    [1, 3, 5],          # 0 Passed
    [0, 5, 6],          # 1 Passed
    [-4, -2, 0, 1, 3],  # 2 Passed
    [0, 3, 3],          # 3 Passed
    [],                 # 4 Passed
)
arr = test_cases[4]
print(sortedSquared(arr))
