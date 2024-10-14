'''PROGRAMA EXEMPLO 7: SendoS = + + + + +
1
1
3
2
5
3
7
4
99
50
... , faça um programa que calcule e mostreo valor de S.'''

#
sum = 0
numerator = 1
denominator = 1
# Program presentation
print("Calculation of the series: \n")
print("S = 1 + 3/2 + 5/3 + 7/4 + ... 99/50\n\n")
# Calculation of the series
for i in range(50):
 sum += numerator/denominator
numerator += 2
denominator += 1
# Result
print(f"Result: {sum:,.2f}")