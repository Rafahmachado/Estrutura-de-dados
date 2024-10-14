''' Elabore um programa que calcule e mostre a soma dos 10 primeiros termos da série:'''

import math

# Inicializa a soma
soma = 0

# Loop para calcular a soma dos 10 primeiros termos
for i in range(10):
    numerador = 100 - i
    denominador = math.factorial(i)
    termo = numerador / denominador
    soma += termo

# Exibe a soma dos 10 primeiros termos
print(f"A soma dos 10 primeiros termos da série é: {soma}")
