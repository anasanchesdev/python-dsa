"""
Uma lista monótona é exclusivamente não-crescente ou não-decrescente. Termos podem se repetir, mas essa lista não pode
ser não-crescente e não-decrescente ao mesmo tempo. Repare que, para ser monótona, a lista pode assumir três formas:
não-decrescente, não-crescente e uniforme. Para cada um destes casos, algumas condições precisam ser atendidas:
- Não-decrescente: se o primeiro elemento da lista for menor que o último, significa que nenhum elemento anterior deve
ser maior que o posterior. Caso contrário, a lista nõa é monótona.
- Não-crescente: se o primeiro elemento da lista for maior que o último, significa que nenhum elemento anterior deve ser
menor que o posterior. Caso contrário, a lista não é monótona.
- Uniforme: se o primeiro elemento da lista for igual ao último, significa que todos os elementos da lista devem ser
iguais. Caso contrário, a lista não é monótona.
"""


def monotonicArray(array):
    length = len(array)
    if length == 0 or length == 1:
        return True
    # NÃO-DECRESCENTE
    if array[0] < array[-1]:
        for index in range(length - 1):
            if array[index] > array[index + 1]:
                return False

    # NÃO-CRESCENTE
    elif array[0] > array[-1]:
        for index in range(length - 1):
            if array[index] < array[index + 1]:
                return False
    # UNIFORME
    else:
        for index in range(length - 1):
            if array[index] != array[index + 1]:
                return False

    return True


test_cases = (
    [1, 2, 3, 4],   # 0 Passed
    [1, 2, 3, 3],   # 1 Passed
    [3, 2, 1, 0],   # 2 Passed
    [1, 1, 1, 1],   # 3 Passed
    [1],            # 4 Passed
    [],             # 5 Passed
    [2, 2, 3, 1],   # 6 Passed
    [3, 1, 3, 1],   # 7 Passed
)

print(monotonicArray(test_cases[1]))
