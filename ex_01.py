'''Elabore um programa que: Mostre um menu de opções de conversão entre moedas 
dólar americano,euro,libra esterlina e  yuan;

Leia a escolha do usuário;
Leia o custo em R$ (reais) da operação;
Imprima o valor da transação n '''

# Criando função: menu de opções de conversão entre as moedas ,e fazer a conversão para valor da moeda brasileira
def mostrar_menu():
    print("Escolha a moeda para conversão:")
    print("1 – Dólar Americano")
    print("2 – Euro")
    print("3 – Libra Esterlina")
    print("4 – Yuan")

def obter_fator_conversao(opcao):
    if opcao == 1:
        return 3.258
    elif opcao == 2:
        return 4.095
    elif opcao == 3:
        return 4.529
    elif opcao == 4:
        return 0.515
    else:
        return None

def converter_moeda(valor_reais, fator_conversao):
    return valor_reais / fator_conversao

def main():
    mostrar_menu()
    opcao = int(input("Digite a opção desejada: "))
    fator_conversao = obter_fator_conversao(opcao)
    
    if fator_conversao is None:
        print("Opção inválida!")
        return
    
    valor_reais = float(input("Digite o valor em R$ (reais): "))
    valor_convertido = converter_moeda(valor_reais, fator_conversao)
    
    if opcao == 1:
        moeda = "Dólares Americanos"
    elif opcao == 2:
        moeda = "Euros"
    elif opcao == 3:
        moeda = "Libras Esterlinas"
    elif opcao == 4:
        moeda = "Yuans"
    
    print(f"O valor da transação é: {valor_convertido:.2f} {moeda}")

if __name__ == "__main__":
    main()


# para executar python ex_01.py
