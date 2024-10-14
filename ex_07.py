'''Para fazer o balanço mensal de um armazém, faça um programa que que leia para um número 
qualquer de mercadorias diferentes o preço de custo, o preço de venda e a quantidade vendida. 
 A partir desses dados imprima: o número total de mercadorias diferentes lidas, 
o faturamento total e o lucro total do armazém.'''


def balanco_mensal():#pega os dados das mercadorias até que o usuário digite sair
    mercadorias = []
    
    while True:
        nome = input("Digite o nome da mercadoria (ou 'sair' para terminar): ")
        if nome.lower() == 'sair':
            break
        preco_custo = float(input(f"Digite o preço de custo de {nome}: "))
        preco_venda = float(input(f"Digite o preço de venda de {nome}: "))
        quantidade_vendida = int(input(f"Digite a quantidade vendida de {nome}: "))
        
        mercadoria = {
            'nome': nome,
            'preco_custo': preco_custo,
            'preco_venda': preco_venda,
            'quantidade_vendida': quantidade_vendida
        }
        mercadorias.append(mercadoria)
    
    total_mercadorias = len(mercadorias)
    faturamento_total = sum(m['preco_venda'] * m['quantidade_vendida'] for m in mercadorias)
    lucro_total = sum((m['preco_venda'] - m['preco_custo']) * m['quantidade_vendida'] for m in mercadorias)
    
    print(f"\nNúmero total de mercadorias diferentes: {total_mercadorias}")
    print(f"Faturamento total: R${faturamento_total:.2f}")
    print(f"Lucro total: R${lucro_total:.2f}")

# Chama a função para executar o programa
balanco_mensal()

# Definição da Função balanco_mensal():

# Esta função realiza o balanço mensal das mercadorias, coletando informações sobre cada mercadoria e calculando o total de mercadorias, o faturamento total e o lucro total.
# Inicialização da Lista mercadorias:

# mercadorias = [] cria uma lista vazia para armazenar dicionários, cada um representando uma mercadoria.
# Loop de Entrada de Dados:

# while True: inicia um loop infinito que só será interrompido quando o usuário optar por sair.
# nome = input("Digite o nome da mercadoria (ou 'sair' para terminar): ") solicita o nome da mercadoria. Se o usuário digitar 'sair', o loop é interrompido (if nome.lower() == 'sair': break).
# preco_custo, preco_venda, e quantidade_vendida são lidos e convertidos para os tipos adequados (float e int).
# Armazenamento das Informações:

# Um dicionário mercadoria é criado para armazenar as informações da mercadoria: nome, preço de custo, preço de venda e quantidade vendida.
# Este dicionário é adicionado à lista mercadorias com mercadorias.append(mercadoria).
# Cálculo dos Totais:

# total_mercadorias = len(mercadorias) calcula o número total de mercadorias.
# faturamento_total = sum(m['preco_venda'] * m['quantidade_vendida'] for m in mercadorias) calcula o faturamento total usando uma expressão geradora para somar o faturamento de cada mercadoria.
# lucro_total = sum((m['preco_venda'] - m['preco_custo']) * m['quantidade_vendida'] for m in mercadorias) calcula o lucro total somando o lucro de cada mercadoria.
# Impressão dos Resultados:

# print(f"\nNúmero total de mercadorias diferentes: {total_mercadorias}") imprime o número total de mercadorias.
# print(f"Faturamento total: R${faturamento_total:.2f}") imprime o faturamento total formatado com duas casas decimais.
# print(f"Lucro total: R${lucro_total:.2f}") imprime o lucro total formatado com duas casas decimais.
# Chamada da Função:

# balanco_mensal() é chamada para executar o programa.
# Esse código oferece uma forma organizada de registrar e analisar o desempenho de mercadorias em um armazém, facilitando o controle financeiro e a tomada de decisões.









# Função balanco_mensal():

# Coleta dados sobre várias mercadorias até o usuário digitar "sair".
# Para cada mercadoria, o código lê o nome, preço de custo, preço de venda e quantidade vendida.
# Armazenamento e Processamento:

# Armazena os dados de cada mercadoria em uma lista.
# Calcula o total de mercadorias, o faturamento total e o lucro total usando esses dados.
# Saída dos Resultados:

# Imprime o número total de mercadorias, o faturamento total e o lucro total.
# O programa ajuda a gerenciar e analisar o desempenho financeiro das mercadorias em um armazém.