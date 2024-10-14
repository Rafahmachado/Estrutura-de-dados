'''. Faça um programa didático para estudo de tabuadas de 1 até 10, onde:

a. A criança escolhe a tabuada a ser estudada.
b. O programa gera um número aleatório e pergunta à criança qual o valor dele
multiplicado pela tabuada escolhida. Se a criança errar, o programa pergunta
novamente, se acertar o programa pergunta à criança se ela deseja continuar
respondendo.
c. Ao final, o programa deve imprimir o número de perguntas respondidas, o
número de acertos e o número de erros cometidos pela criança.'''

import random

def tabuada():
    print(" Programa de  estudo de tabuadas!")
    tabuada = int(input("Escolha a tabuada que deseja estudar (1 a 10): "))
    
    acertos = 0
    erros = 0
    perguntas = 0
    
    while True:
        numero = random.randint(1, 10)
        resposta = int(input(f"Qual é o resultado de {tabuada} x {numero}? "))
        perguntas += 1
        
        if resposta == tabuada * numero:
            acertos += 1
            print("Correto! 🎉")
            continuar = input("Deseja continuar? (s/n): ").lower()
            if continuar != 's':
                break
        else:
            erros += 1
            print("Errado. Tente novamente.")
    
    print(f"\nResumo do estudo:")
    print(f"Perguntas respondidas: {perguntas}")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")

if __name__ == "__main__":
    tabuada()
