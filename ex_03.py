#  Em um frigorífico, cada boi é identificado por um cartão que contém seu número e
# seu peso. Faça um programa que leia os números de identificação e o peso de cada
# boi e ao final imprima o número de identificação e o peso do boi mais gordo, do boi
# mais magro e o total de peso dos bois do frigorífico. 


def main():
    # Inicializa variáveis
    bois = []
    total_peso = 0
    
    while True:
        # Lê o número de identificação do boi
        numero = input("Digite o número de identificação do boi (ou 'sair' para finalizar): ")
        
        # Verifica se o usuário quer finalizar o programa
        if numero.lower() == 'sair':
            break
        
        # Lê o peso do boi
        try:
            peso = float(input(f"Digite o peso do boi {numero}: "))
        except ValueError:
            print("Peso inválido. Tente novamente.")
            continue
        
        # Adiciona uma tupla (número, peso) à lista de bois
        bois.append((numero, peso))
        # Soma o peso ao total de peso
        total_peso += peso
    
    # Verifica se a lista de bois não está vazia
    if bois:
        # Encontra o boi mais gordo e o mais magro
        boi_mais_gordo = max(bois, key=lambda boi: boi[1])
        boi_mais_magro = min(bois, key=lambda boi: boi[1])
        
        # Exibe os resultados
        print(f"\nBoi mais gordo: ID {boi_mais_gordo[0]}, Peso {boi_mais_gordo[1]} kg")
        print(f"Boi mais magro: ID {boi_mais_magro[0]}, Peso {boi_mais_magro[1]} kg")
        print(f"Peso total dos bois: {total_peso} kg")
    else:
        print("Nenhum boi foi registrado.")

if __name__ == "__main__":
    main()
