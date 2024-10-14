# 1. O volume de uma esfera pode ser calculado pela fórmula 
# V=4/3 Pir*3, onde r é o raio da esfera. Faça um programa que imprima uma tabela de volumes para esferas que 
# tenham raios entre 0 e 15 cm, de 0.5 em 0.5cm.
import math

def calcular_volume(raio):
    return (4/3) * math.pi * raio**3

print(f"{'Raio (cm)':<10} {'Volume (cm³)':<15}")
for r in range(0, 31):
    raio = r * 0.5
    volume = calcular_volume(raio)
    print(f"{raio:<10} {volume:<15.2f}")
