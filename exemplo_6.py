'''PROGRAMA EXEMPLO 6: Faça um programa que leia um conjunto de números positivos,
 encerrando quando for digitado um número negativo ou zero e imprima o menor número lido.
 SOLUÇÃO:'''

number = -1
while number <= 0:
 number = int(input("Enter a positive number: "))
if number <= 0:
 print('\tYou need to enter a positive number!\n')
 smaller = number # the first number is used as a reference
while number > 0:
   number = int(input("Enter a positive number: "))
if number < smaller and number > 0:
   smaller = number
print(f"Smallest number: {smaller}")