'''O seno de um ângulo em radianos, no intervalo de 0 à2
r/2 pode ser calculado através da série de McLaurin, apresentada a seguir:
sen x = x/1!-x*3/3%+x*3/5!-x*3/7+...


a. Escreva uma função que converta um ângulo em graus para seu valor em
radianos (rad180 = r rad )
b. Escreva uma função que receba como parâmetro um ângulo em graus, a
precisão requerida para o cálculo e retorne o seu seno, utilizando a função de
conversão graus-radiano feita anteriormente
c. Faça um programa que teste a sua função para cálculo do seno.'''


import math

# a. Função para converter graus em radianos
def graus_para_radianos(graus):
    return graus * (math.pi / 180)

# b. Função para calcular o seno usando a série de Maclaurin
def seno_maclaurin(radianos, precisao):
    seno = 0
    termo = radianos
    n = 1
    while abs(termo) > precisao:
        seno += termo
        termo *= -radianos**2 / ((2*n) * (2*n + 1))
        n += 1
    return seno

def seno_angulo(graus, precisao):
    radianos = graus_para_radianos(graus)
    return seno_maclaurin(radianos, precisao)

# c. Programa para testar a função de cálculo do seno
def main():
    angulo = float(input("Digite o ângulo em graus: "))
    precisao = float(input("Digite a precisão desejada: "))
    seno = seno_angulo(angulo, precisao)
    print(f"O seno de {angulo} graus é aproximadamente {seno}")

if __name__ == "__main__":
    main()
