'''Para fazer uma pesquisa sobre o consumo de energia elétrica de uma cidade, são
fornecidos os seguintes dados:
• O preço o kWh
• O número de identificação de cada consumidor
• A quantidade de kWh consumido no mês por cada um
• O código do tipo de consumidor (residencial, comercial ou industrial)

A partir desses dados calcule:
a. Para cada consumidor, o total a pagar;
b. O maior consumo verificado;
c. O menor consumo verificado
d. O total de consumo (em kWh) para cada um dos três tipos de consumidores
e. A média de consumo (em kWh) para cada um dos três tipos de consumidores
f. O total arrecadado pela companhia elétrica'''

def main():
    # Constantes
    preco_kwh = float(input("Digite o preço do kWh: "))
    
    consumidores = []
    total_consumo_residencial = 0
    total_consumo_comercial = 0
    total_consumo_industrial = 0
    total_arrecadado = 0

    while True:
        identificacao = input("Digite o número de identificação do consumidor (ou '0' para finalizar): ")
        if identificacao == '0':
            break
        kwh_consumido = float(input("Digite a quantidade de kWh consumido no mês: "))
        tipo_consumidor = input("Digite o código do tipo de consumidor (residencial, comercial, industrial): ").lower()
        
        total_a_pagar = kwh_consumido * preco_kwh
        consumidores.append({
            "ID": identificacao,
            "kWh Consumido": kwh_consumido,
            "Tipo": tipo_consumidor,
            "Total a Pagar": total_a_pagar
        })
        
        total_arrecadado += total_a_pagar
        
        if tipo_consumidor == "residencial":
            total_consumo_residencial += kwh_consumido
        elif tipo_consumidor == "comercial":
            total_consumo_comercial += kwh_consumido
        elif tipo_consumidor == "industrial":
            total_consumo_industrial += kwh_consumido

    if consumidores:
        maior_consumo = max(consumidores, key=lambda x: x["kWh Consumido"])
        menor_consumo = min(consumidores, key=lambda x: x["kWh Consumido"])
        
        total_consumidores_residenciais = sum(1 for c in consumidores if c["Tipo"] == "residencial")
        total_consumidores_comerciais = sum(1 for c in consumidores if c["Tipo"] == "comercial")
        total_consumidores_industriais = sum(1 for c in consumidores if c["Tipo"] == "industrial")
        
        media_consumo_residencial = total_consumo_residencial / total_consumidores_residenciais if total_consumidores_residenciais else 0
        media_consumo_comercial = total_consumo_comercial / total_consumidores_comerciais if total_consumidores_comerciais else 0
        media_consumo_industrial = total_consumo_industrial / total_consumidores_industriais if total_consumidores_industriais else 0
        
        print("\nResumo dos Consumidores:")
        for consumidor in consumidores:
            print(f"ID: {consumidor['ID']}, kWh Consumido: {consumidor['kWh Consumido']}, Tipo: {consumidor['Tipo']}, Total a Pagar: R${consumidor['Total a Pagar']:.2f}")
        
        print(f"\nMaior consumo verificado: {maior_consumo['kWh Consumido']} kWh (ID: {maior_consumo['ID']})")
        print(f"Menor consumo verificado: {menor_consumo['kWh Consumido']} kWh (ID: {menor_consumo['ID']})")
        print(f"Total de consumo residencial: {total_consumo_residencial} kWh")
        print(f"Total de consumo comercial: {total_consumo_comercial} kWh")
        print(f"Total de consumo industrial: {total_consumo_industrial} kWh")
        print(f"Média de consumo residencial: {media_consumo_residencial:.2f} kWh")
        print(f"Média de consumo comercial: {media_consumo_comercial:.2f} kWh")
        print(f"Média de consumo industrial: {media_consumo_industrial:.2f} kWh")
        print(f"Total arrecadado pela companhia elétrica: R${total_arrecadado:.2f}")
    else:
        print("Nenhum dado de consumidor foi registrado.")

if __name__ == "__main__":
    main()
