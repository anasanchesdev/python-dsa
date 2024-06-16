"""
S, T = O(n)
TWO POINTERS TECHNIQUE (técnica dos dois ponteiros)
- Ponteiros são números que indicam duas posições distintas de uma lista;
- Neste algoritmo, "first" é o primeiro elemento da lista, inicializado como 0, e "last" é o último elemento da
lista, inicializado como a última posição da lista;
- É inicializada uma lista de elementos nulos que assume o mesmo tamanho da lista original, com o intuito de servir
como base para os elementos ao quadrado conforme as devidas comparações;
- São inicializados os dois ponteiros: first, que aponta para o primeiro elemento da lista, e last, que aponta para o
último elemento da lista;
- O algoritmo funciona da seguinte forma: como vamos elevar os números ao quadrado, quanto mais próximo o número for da
borda da lista, mais chances ele tem de ser o maior item da lista (reta real) e de ocupar as últimas posições da lista
final. Portanto, começamos comparando o resultado ao quadrado do primeiro número da lista com o último pois, com
certeza, um deles será o maior, tendo em mente o fato de que as listas dadas como input são sempre crescentes. O
ponteiro do número que for o maior da iteração moverá uma posição em direção ao centro da lista, enquanto o outro
permance inalterado. O maior número assumirá a posição "index" em "new_array";
- Além disso, no início do algoritmo é verificado se a lista é vazia, uma vez que uma das condições do problema é que,
caso a lista seja vazia, deve-se retornar a própria lista. Esta verificação é feita logo no início do código para evitar
operações desnecessárias.
- Sendo assim, o algoritmo possui complexidade de tempo O(n), pois passa por cada elemento do input apenas uma vez e
complexidade de espaço também O(n), pois cria uma nova lista "new_array" de mesmo tamanho do input.
"""


def sortedSquared(array):
    if not array:
        return array
    length = len(array)
    new_array = [0] * length
    first, last = 0, length - 1
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
