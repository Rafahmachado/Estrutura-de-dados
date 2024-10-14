''' Uma empresa está fazendo um estudo de possibilidades de aumento aos seus
funcionários e deseja saber se é mais vantajoso dar um aumento uniforme de 10% à
todos os funcionários ou seguir a seguinte tabela progressiva:

Salário Percentual de aumento
até R$1000,00 15%
até R$2000,00 10%
acima de R$2000,00 5%

Faça um programa que leia o salário de um número qualquer de funcionários,
imprimindo para cada um o novo salário nos dois casos (aumento uniforme ou
aumento progressivo). Ao final, o programa deve fornecer:
a. O total de funcionários
b. O salário médio dos funcionários
c. O total da folha de pagamentos atual
d. O total da folha de pagamentos futura nos dois casos estudados, indicando
qual o caminho mais econômico para a empresa.'''

def aumento_uniforme(salario):
    return salario * 1.10

def aumento_progressivo(salario):
    if salario <= 1000:
        return salario * 1.15
    elif salario <= 2000:
        return salario * 1.10
    else:
        return salario * 1.05

def main():
    salarios = []
    
    while True:
        salario = float(input("Digite o salário do funcionário (ou '0' para finalizar): "))
        if salario == 0:
            break
        salarios.append(salario)
    
    total_funcionarios = len(salarios)
    total_salarios_atual = sum(salarios)
    total_uniforme = sum(aumento_uniforme(salario) for salario in salarios)
    total_progressivo = sum(aumento_progressivo(salario) for salario in salarios)
    salario_medio = total_salarios_atual / total_funcionarios if total_funcionarios > 0 else 0
    
    print("\nResumo dos Salários:")
    for salario in salarios:
        novo_salario_uniforme = aumento_uniforme(salario)
        novo_salario_progressivo = aumento_progressivo(salario)
        print(f"Salário atual: R${salario:.2f}, Novo salário (uniforme): R${novo_salario_uniforme:.2f}, Novo salário (progressivo): R${novo_salario_progressivo:.2f}")
    
    print(f"\nTotal de funcionários: {total_funcionarios}")
    print(f"Salário médio dos funcionários: R${salario_medio:.2f}")
    print(f"Total da folha de pagamentos atual: R${total_salarios_atual:.2f}")
    print(f"Total da folha de pagamentos futura (aumento uniforme): R${total_uniforme:.2f}")
    print(f"Total da folha de pagamentos futura (aumento progressivo): R${total_progressivo:.2f}")
    
    if total_uniforme > total_progressivo:
        print("O aumento progressivo é mais econômico para a empresa.")
    else:
        print("O aumento uniforme é mais econômico para a empresa.")

if __name__ == "__main__":
    main()

