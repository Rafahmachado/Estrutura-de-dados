''' O número 3025 possui a interessante característica:
30 + 25 = 55
552 = 3025

Faça um programa que procure todos os números de 4 algarismos que possuem essa
característica'''


# Loop para verificar todos os números de 4 algarismos
for i in range(1000, 10000):
    # Divide o número em duas partes
    div = i // 100
    resto = i % 100
    
    # Calcula a soma das duas partes
    soma = div + resto
    
    # Verifica se o quadrado da soma é igual ao número original
    if soma * soma == i:
        print(i)
