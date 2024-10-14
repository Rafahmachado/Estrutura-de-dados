'''Fazer um programa que calcule e escreva o número de grãos de milho que podem ser 
colocados em um tabuleiro de xadrez, colocando 1 no primeiro quadro e nos quadros 
seguintes o dobro do quadro anterior. Obs.: esse número cresce muito rápido, tenha 
o cuidado de testar se ele não sofre um overflow.'''



graos = 1
total = 0
contador = 1

while contador <= 64: 
    total += graos 
    graos *= 2    
    contador += 1  

print(total)


# Este algoritmo calcula o número total de grãos de trigo que seriam 
# colocados em um tabuleiro de xadrez, se a quantidade de grãos dobrasse em cada quadrado,
#  começando com 1 grão no primeiro quadrado. O tabuleiro de xadrez tem 64 quadrados,
#  então o loop itera 64 vezes, dobrando o número de grãos a cada iteração e acumulando o total.





