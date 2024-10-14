''' A série de Fibbonacci é gerada da seguinte forma: os dois primeiros termos são 1, os 
demais são dados pela soma dos dois anteriores. Faça um programa que imprima os 
“n” primeiros termos da série, sendo “n” dado pelo usuário.'''

# Solicita ao usuário o número de termos
n = int(input("Digite o número de termos da série de Fibonacci: "))

# dois primeiros termos da série,sendo “n” dado pelo usuário.
a, b,c = 0, 1 ,1

# Imprime os dois primeiros termos
print(a, b, end=" ")

# Gera e imprime os termos seguintes
for _ in range(n - 2):
    a, b = b, a + b
    print(b, end=" ")


# Sayonnara essa seria minha outra tentativa,compare com a sua ok!!

# t1 = 0
# t2 = 1

# n = int(input('Quantos termos da sequência de Fibonacci você quer?  '))
# c = 0

# while c < n:
#     t3 = t1 + t2
#     print(t1, end=' - ')
#     t1 = t2
#     t2 = t3
#     c = c + 1
# print(t2, end='')