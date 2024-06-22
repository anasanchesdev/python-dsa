"""
                0
           0          1
        0    1      1    0
       0 1  1 0    1 0  0 1
              [...]
n
1| 0
2| 01
3| 0110
4| 011101001

Propriedades da sequência:
- Toda primeira metade da linha n é idêntica à primeira metade da linha n anterior (n - 1)
- Toda segunda metade da linha n é idêntica ao inverso (NOT) da segunda metade da linha n anterior (n - 1)
Levando em conta estas propriedades, para achar o valor de k em n é preciso verificar se k se encontra na primeira
metade ou na segunda metade de n e agir de acordo:
- Se estiver na primeira metade de n, k é o próprio elemento de n anterior (n - 1)
- Se estiver na segunda metade de n, k é o elemento de n anterior inverso (n - 1)'

Exemplo (k na segunda metade):
n = 4, k = 7, mid (posição de k na linha anterior) = 7 // 4 = 3
n
3| 01(1)0
4| 011010(0)1

k em n = 0
k em n-1 = 1
Logo, k = 1' = 0
(' -> notação de not)

"""


def kthSymbol(n, k):
    if n == 1:  # condição de término
        return 0

    mid = 2**(n-1) // 2  # divisão inteira, posição de k na linha anterior
    if k <= mid:
        return kthSymbol(n - 1, k)
    else:
        return int(not kthSymbol(n - 1, k - mid))


print(kthSymbol(4, 7))
