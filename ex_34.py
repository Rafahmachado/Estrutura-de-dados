''' Uma equação do segundo grau é escrita02 =++ cbxax e a sua solução é dada em
função dos valores de a, b e c. Podendo ter duas raízes, uma ou nenhuma. Escreva
uma função que resolva a equação do segundo grau, retornando o número de raízes
encontradas. Os valores dessas raízes devem ser retornados em parâmetros.'''

import math

def resolver_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 0, None, None  # Nenhuma raiz real
    elif delta == 0:
        x = -b / (2*a)
        return 1, x, None  # Uma raiz real
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return 2, x1, x2  # Duas raízes reais

# Testando a função para retornar em parâmetros 
num_raizes, raiz1, raiz2 = resolver_equacao_segundo_grau(1, -3, 2)
print(f"Número de raízes: {num_raizes}, Raiz 1: {raiz1}, Raiz 2: {raiz2}")
