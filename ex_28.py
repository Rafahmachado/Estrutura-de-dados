'''Em uma loja de eletrodomésticos, os funcionários da seção de TVs recebem,
mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação
ao tipo e número de televisores vendidos, de acordo com a tabela abaixo:
Tipo Quantidade vendida Comissões
8 K 10 ou mais R$ 550 por TV vendida
Menos que 10 R$ 350 por TV vendida
4 K 10 ou mais R$ 420 por TV vendida
Menos que 10 R$ 250 por TV vendida
Sabe-se ainda, que ele tem um desconto de 8% do salário total para pagamento do
INSS e se o seu salário total for superior a R$ 950,00 ele ainda tem um desconto de
12
5% do salário para fins de imposto de renda. Faça um programa que leia os dados de
vários funcionários e, para cada funcionário, calcule e imprima o salário líquido (já
com os descontos). Além disso, no final, o programa deve:
a. Imprimir o número de funcionários.
b. Imprimir o total de salários pagos.
c. Imprimir a média das comissões.
d. Imprimir o valor da maior e da menor comissão paga pelo departamento'''

def calcular_comissao(tipo_tv, quantidade):
    if tipo_tv == "8k":
        if quantidade >= 10:
            return 550 * quantidade
        else:
            return 350 * quantidade
    elif tipo_tv == "4k":
        if quantidade >= 10:
            return 420 * quantidade
        else:
            return 250 * quantidade
    return 0

def calcular_salario_liquido(salario_fixo, comissao):
    salario_bruto = salario_fixo + comissao
    desconto_inss = salario_bruto * 0.08
    salario_apos_inss = salario_bruto - desconto_inss
    desconto_ir = salario_apos_inss * 0.05 if salario_apos_inss > 950 else 0
    salario_liquido = salario_apos_inss - desconto_ir
    return salario_liquido, comissao

def main():
    funcionarios = []
    total_comissao = 0
    
    while True:
        nome = input("Digite o nome do funcionário (ou 'sair' para finalizar): ")
        if nome.lower() == 'sair':
            break
        salario_fixo = float(input("Digite o salário fixo do funcionário: "))
        tipo_tv = input("Digite o tipo de TV vendida (8k/4k): ").lower()
        quantidade = int(input("Digite a quantidade de TVs vendidas: "))
        
        comissao = calcular_comissao(tipo_tv, quantidade)
        salario_liquido, comissao = calcular_salario_liquido(salario_fixo, comissao)
        
        funcionarios.append({
            "nome": nome,
            "salario_liquido": salario_liquido,
            "comissao": comissao
        })
        total_comissao += comissao
    
    total_funcionarios = len(funcionarios)
    total_salarios = sum(funcionario["salario_liquido"] for funcionario in funcionarios)
    media_comissao = total_comissao / total_funcionarios if total_funcionarios > 0 else 0
    maior_comissao = max(funcionarios, key=lambda x: x["comissao"], default={"comissao": 0})["comissao"]
    menor_comissao = min(funcionarios, key=lambda x: x["comissao"], default={"comissao": 0})["comissao"]
    
    print(f"\nTotal de funcionários: {total_funcionarios}")
    print(f"Total de salários pagos: R${total_salarios:.2f}")
    print(f"Média das comissões: R${media_comissao:.2f}")
    print(f"Maior comissão paga: R${maior_comissao:.2f}")
    print(f"Menor comissão paga: R${menor_comissao:.2f}")

if __name__ == "__main__":
    main()
