'''Elaborar um programa que calcule e mostre o fatorial de um número
(N!),sendo que N é fornecido pelo usuário'''

# import math

# # Solicita ao usuário que insira um número
# numero = int(input("Digite um número para calcular o fatorial: "))
# resultado = math.factorial(numero)

# # Construir a string de saída
# saida = f"Cálculo de {numero}! = "
# for i in range(numero, 0, -1):
#     saida += f"{i} x " if i > 1 else f"{i} = "

# saida += str(resultado)
# print(saida)


#sayonnara.outra opção
from math import factorial

n = int(input('digite um número para calcular seu fatorial:'))

f = factorial(n)
print('O fatorial de {} é {}'.format(n,f))

