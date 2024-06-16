def sortedSquared(array):

    if not array:
        return array

    # elevar todos os números ao quadrado
    # T = O(n)
    length = len(array)
    for n in range(length):
        array[n] = array[n] ** 2

    # T = O(n²)
    for i in range(length):
        for j in range(length):
            if array[i] < array[j]:
                temp = array[j]
                array[j] = array[i]
                array[i] = temp
            print(array)
    return array


test_cases = (
    [1, 3, 5],          # 0 Passed
    [0, 5, 6],          # 1 Passed
    [-4, -2, 0, 1, 3],  # 2 Passed
    [0, 3, 3],          # 3 Passed
    [],                 # 4 Passed
)
arr = test_cases[0]
print(sortedSquared(arr))


# T = O(n²)
# S = O(1)
