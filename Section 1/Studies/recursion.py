# def function(n):
#     if n > 5:
#         return None
#     print(n)
#     function(n + 1)

# def function(n):  # fatorial
#     if n == 1:
#         return 1
#     return function(n - 1) * n

def function(n):
    if n == 0:  # condição de término básica
        return None
    print(n)  # problema original
    function(n - 1)  # problema secundário
    print(n)  # problema original


print(function(5))
