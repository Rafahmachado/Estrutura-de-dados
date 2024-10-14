'''Escreva uma função (FparaC) que receba uma temperatura em graus F e retorne a
temperatura em graus C, sendo:)32(
9
5 −= FC . A seguir, faça um programa que, em
loop, leia um valor para F da entrada padrão e o imprima o valor de C correspondente,
utilizando a função FparaC'''

def FparaC(fahrenheit):
    return (5/9) * (fahrenheit - 32)

while True:
    try:
        f = float(input("Digite a temperatura em Fahrenheit (ou 'q' para sair): "))
        c = FparaC(f)
        print(f"{f}°F é igual a {c:.2f}°C")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número ou 'q' para sair.")
