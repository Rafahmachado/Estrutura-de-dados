''' Faça um programa que apresente na tela um menu com as seguintes opções: 
1.Converter um ângulo em graus para radiano;
2. Calcular o seno de um ângulo, 
3.Calcular o valor de . 
4. Resolver uma equação do segundo grau; 0. Sair.
 Depois de

feita a opção, o programa deve chamar uma função que leia do usuário os parâmetros
necessários para o cálculo escolhido e a seguir usar uma das funções que você já
implementou'''

import math

def graus_para_radianos(graus):
    return graus * (math.pi / 180)

def seno_maclaurin(radianos, precisao):
    seno = 0
    termo = radianos
    n = 1
    while abs(termo) > precisao:
        seno += termo
        termo *= -radianos**2 / ((2*n) * (2*n + 1))
        n += 1
    return seno

def cosseno_maclaurin(radianos, precisao):
    cosseno = 0
    termo = 1
    n = 0
    while abs(termo) > precisao:
        cosseno += termo
        termo *= -radianos**2 / ((2*n + 1) * (2*n + 2))
        n += 1
    return cosseno

def resolver_equacao_segundo_grau(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return 0, None, None  # Nenhuma raiz real
    elif delta == 0:
        x = -b / (2*a)
        return 1, x, None  # Uma raiz real
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return 2, x1, x2  # Duas raízes reais

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Converter um ângulo em graus para radianos")
        print("2. Calcular o seno de um ângulo")
        print("3. Calcular o cosseno de um ângulo")
        print("4. Resolver uma equação do segundo grau")
        print("0. Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            graus = float(input("Digite o ângulo em graus: "))
            radianos = graus_para_radianos(graus)
            print(f"{graus} graus é igual a {radianos} radianos")
        elif opcao == 2:
            graus = float(input("Digite o ângulo em graus: "))
            precisao = float(input("Digite a precisão desejada: "))
            radianos = graus_para_radianos(graus)
            seno = seno_maclaurin(radianos, precisao)
            print(f"O seno de {graus} graus é aproximadamente {seno}")
        elif opcao == 3:
            graus = float(input("Digite o ângulo em graus: "))
            precisao = float(input("Digite a precisão desejada: "))
            radianos = graus_para_radianos(graus)
            cosseno = cosseno_maclaurin(radianos, precisao)
            print(f"O cosseno de {graus} graus é aproximadamente {cosseno}")
        elif opcao == 4:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            num_raizes, raiz1, raiz2 = resolver_equacao_segundo_grau(a, b, c)
            print(f"Número de raízes: {num_raizes}")
            if num_raizes > 0:
                print(f"Raiz 1: {raiz1}")
            if num_raizes > 1:
                print(f"Raiz 2: {raiz2}")
        elif opcao == 0:
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
