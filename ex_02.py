#  Faça um programa que leia um conjunto de números positivos, sendo o conjunto  
# destes números finalizado quando for digitado um número negativo. Ao final, 
# imprima o maior e o menor número lido e a média deles.


def main():
  
    numeros = []
    
    while True:
       
        numero = float(input("Digite um número positivo (ou um número negativo para finalizar): "))
        
        # Verifica se o número é negativo para encerrar o loop
        if numero < 0:
            break
        
        # Adiciona o número à lista de números
        numeros.append(numero)
    
    # Verifica se a lista não está vazia
    if numeros:
        maior = max(numeros)
        menor = min(numeros)
        media = sum(numeros) / len(numeros)
        
        # Exibe os resultados
        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("Nenhum número positivo foi inserido.")

if __name__ == "__main__":
    main()
