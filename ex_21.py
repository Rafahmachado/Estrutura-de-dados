''' Faça um programa didático para estudo das raízes quadradas dos números, da
seguinte forma: o programa gera um número aleatório, eleva ao quadrado e pergunta
qual a raiz quadrada desse valor para o estudante. O programa deve apresentar as
mensagens de erro e incentivo e os números de perguntas, acertos e erros de forma
semelhante aos anteriores.'''

import random

def estudo_raizes_quadradas():
    print("Bem-vindo ao programa de estudo de raízes quadradas!")
    
    acertos = 0
    erros = 0
    perguntas = 0
    
    while True:
        numero = random.randint(1, 100)
        quadrado = numero ** 2
        perguntas += 1
        
        resposta = int(input(f"Qual é a raiz quadrada de {quadrado}? "))
        
        if resposta == numero:
            acertos += 1
            print("Correto! 🎉")
            continuar = input("Deseja continuar? (s/n): ").lower()
            if continuar != 's':
                break
        else:
            erros += 1
            print(f"Errado. A resposta correta é {numero}. Tente novamente.")
    
    print(f"\nResumo do estudo:")
    print(f"Perguntas respondidas: {perguntas}")
    print(f"Acertos: {acertos}")
    print(f"Erros: {erros}")

if __name__ == "__main__":
    estudo_raizes_quadradas()
