'''Escreva as seguintes funções:
a. CparaF – faz a conversão de uma temperatura em graus C para graus F.
b. CparaK – faz a conversão de uma temperatura em C para Kelvin (C=K-273)
c. KparaC – faz a conversão de K para C.
d. KparaF – faz a conversão de K para F (dica: utilize as funções anteriores)
e. FparaK – faz a conversão de F para K.
A seguir, faça um programa que apresente continuamente um menu na tela com
todas as opções de conversão que você implementou. Uma vez feita a opção, o
programa lê do teclado o valor a ser convertido e imprime o resultado'''



# a. Converte Celsius para Fahrenheit
def CparaF(celsius):
    return (celsius * 9/5) + 32

# b. Converte Celsius para Kelvin
def CparaK(celsius):
    return celsius + 273.15

# c. Converte Kelvin para Celsius
def KparaC(kelvin):
    return kelvin - 273.15

# d. Converte Kelvin para Fahrenheit
def KparaF(kelvin):
    celsius = KparaC(kelvin)
    return CparaF(celsius)

# e. Converte Fahrenheit para Kelvin
def FparaK(fahrenheit):
    celsius = FparaC(fahrenheit)
    return CparaK(celsius)

# Função auxiliar para converter Fahrenheit para Celsius
def FparaC(fahrenheit):
    return (5/9) * (fahrenheit - 32)

# Testando as funções
print(CparaF(0))  # 32.0
print(CparaK(0))  # 273.15
print(KparaC(273.15))  # 0.0
print(KparaF(273.15))  # 32.0
print(FparaK(32))  # 273.15
