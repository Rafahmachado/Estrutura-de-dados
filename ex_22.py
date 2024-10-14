


'''Calcule e mostre o imposto de renda de um grupo de contribuintes considerando que
os dados de cada contribuinte (número do CPF, número de dependentes e renda
mensal) são valores fornecidos pelo usuário. Para cada contribuinte será feito um
desconto no imposto de 5% do salário mínimo (R$136,00) para cada dependente (o
salário mínimo e o desconto são designados por constantes simbólicas). Os valores
da alíquota para cálculo do imposto são:

Renda Líquida (R$) Alíquota

até 900,00 isento
900,01 até 1500,00 5%
1500,01 até 1900,00 10%
1900,01 até 2200,00 15%
acima de 2200,01 20%
acima de 2200,01 20%
O último valor, que não será considerado, terá o número do CPF igual a zero. Ao final,
devem ser impressos:
a. Para cada contribuinte, o total a pagar.
b. O número de contribuintes.
c. O total de contribuintes isentos e não isentos.
d. O total de impostos que serão arrecadados desse grupo de contribuintes.
e. O número do CPF e o valor da contribuição daquele contribuinte que for pagar
o maior imposto'''

# Constantes
SALARIO_MINIMO = 136.00
DESCONTO_DEPENDENTE = 0.05 * SALARIO_MINIMO

def calcular_imposto(renda_liquida):
    if renda_liquida <= 900.00:
        return 0.00
    elif renda_liquida <= 1500.00:
        return renda_liquida * 0.05
    elif renda_liquida <= 1900.00:
        return renda_liquida * 0.10
    elif renda_liquida <= 2200.00:
        return renda_liquida * 0.15
    else:
        return renda_liquida * 0.20

def main():
    contribuintes = []
    total_isentos = 0
    total_nao_isentos = 0
    total_impostos = 0.00
    maior_imposto = 0.00
    cpf_maior_imposto = ""

    while True:
        cpf = input("Digite o CPF do contribuinte (ou '0' para finalizar): ")
        if cpf == '0':
            break
        dependentes = int(input("Digite o número de dependentes: "))
        renda_mensal = float(input("Digite a renda mensal: "))
        
        desconto_total = dependentes * DESCONTO_DEPENDENTE
        renda_liquida = renda_mensal - desconto_total
        imposto = calcular_imposto(renda_liquida)
        
        if imposto == 0.00:
            total_isentos += 1
        else:
            total_nao_isentos += 1
            total_impostos += imposto
            if imposto > maior_imposto:
                maior_imposto = imposto
                cpf_maior_imposto = cpf
        
        contribuintes.append({
            "CPF": cpf,
            "Dependentes": dependentes,
            "Renda Mensal": renda_mensal,
            "Renda Líquida": renda_liquida,
            "Imposto": imposto
        })
    
    print("\nResumo dos Contribuintes:")
    for contribuinte in contribuintes:
        print(f"CPF: {contribuinte['CPF']}")
        print(f"Dependentes: {contribuinte['Dependentes']}")
        print(f"Renda Mensal: R${contribuinte['Renda Mensal']:.2f}")
        print(f"Renda Líquida: R${contribuinte['Renda Líquida']:.2f}")
        print(f"Imposto a Pagar: R${contribuinte['Imposto']:.2f}\n")
    
    print(f"Número total de contribuintes: {len(contribuintes)}")
    print(f"Total de contribuintes isentos: {total_isentos}")
    print(f"Total de contribuintes não isentos: {total_nao_isentos}")
    print(f"Total de impostos arrecadados: R${total_impostos:.2f}")
    if cpf_maior_imposto:
        print(f"Contribuinte com maior imposto: CPF {cpf_maior_imposto}, Imposto R${maior_imposto:.2f}")

if __name__ == "__main__":
    main()




