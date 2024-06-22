def findTheWinner(n, k):
    i = 1
    out = []
    for _ in range(n):
        i = i + k
        if i > n:
            i = i - n
        out.append(i)
    return i


print(findTheWinner(5, 2))