'''Sendo S= 1-1/2/+/1/3 - 1/4 + 1/5 - .../1/N,
construa um programa que leia N, calcule e mostre o valor da série 
S'''
# Solicita ao usuário para digitar o valor de N
N = int(input("Digite o valor de N: "))

# Inicializa a soma
S = 0

# Loop para calcular a soma da série
for i in range(1, N + 1):
    if i % 2 == 0:
        S -= 1 / i  # Subtrai se o índice for par
    else:
        S += 1 / i  # Adiciona se o índice for ímpar

# Exibe o valor da série
print(f"O valor da série S é: {S}")
