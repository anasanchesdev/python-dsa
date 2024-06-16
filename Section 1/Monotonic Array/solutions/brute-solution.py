def monotonicArray(array):
    length = len(array)
    if length == 0 or length == 1:
        return True
    for index in range(length - 1):
        if array[0] < array[-1] and not array[index] <= array[index + 1] or array[0] > array[-1] and not array[index] >= array[index + 1]:
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

print(monotonicArray(test_cases[3]))
