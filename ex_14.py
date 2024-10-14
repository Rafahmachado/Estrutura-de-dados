''' Construa um programa que calcule e mostre a soma dos 30 primeiros termos da
série: 450/10 + 445/11 + 440/12 + 435/13 + ...'''

soma = 0
numerador = 1
denominador =1

print("Calcular a soma dos 30 primeiros termos")
print("Soma = 1 + 450/10")

soma = 0
numerador = 450
denominador = 10

# Calculo da soma dos 30 primeiros termos
for i in range(30):
    termo = numerador / denominador  # Calcula o termo atual
    soma += termo  # Adiciona o termo à soma
    numerador -= 5  # Decrementa o numerador em 5
    denominador += 1  # Incrementa o denominador em 1

# Soma dos 30 primeiros termos
print(f"A soma dos 30 primeiros termos da série é: {soma}")
