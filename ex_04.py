''' Desejando obter a média aritmética das idades dos alunos do curso de Odontologia,
do primeiro ano, do ano de 2023, construir um programa que leia, calcule e mostre a
 média aritmética das idades. O programa é encerrado quando for lida uma idade igual
a zero e deve rejeitar idades negativas, pedindo que o usuário redigite. '''

def media_aritmetica_idades():
    idades = []  # Lista vazia para armazenar as idades
    
    while True:  # Loop para pedir as idades até que o usuário digite 0
        try:
            idade = int(input("Digite a idade do aluno (ou 0 para encerrar): "))
            if idade == 0:  # Condição para encerrar o programa se a idade for igual a zero
                break
            elif idade < 0:  # Condição para rejeitar idades negativas
                print("Idade inválida. Por favor, digite uma idade positiva.")
                
            else:  # Adiciona a idade à lista se for válida
                idades.append(idade)
        except ValueError:  # Trata entradas que não são números inteiros
            print("Entrada inválida. Por favor, digite um número inteiro.")
    
    if idades:  # Verifica se há idades válidas na lista
        media = sum(idades) / len(idades)
        print(f"A média aritmética das idades é: {media:.2f}")
    else:  # Caso nenhuma idade válida tenha sido inserida
        print("Nenhuma idade válida foi inserida.")

# Chama a função para executar o programa
media_aritmetica_idades()


