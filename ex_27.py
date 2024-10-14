'''O custo de produção de um livro é constituído dos custos por página, mais o custo
de encadernação, além do custo fixo. O custo por página impressa é de R$0,03, o
custo fixo é de R$ 4397,00 e o custo de encadernação depende de cada livro, sendo
utilizada a seguinte tabela:
• Encadernação simples: R$4,30
• Encadernação especial: R$7,80
• Encadernação luxo: R$10,50
Faça um programa que leia para uma lista de livros: o número de páginas, o tipo de
encadernação e o número de vendas previstas (número de cópias) e:
a. Calcule o preço mínimo de cada livro para que cubra os custos de produção e
o preço de venda para que a editora tenha um lucro de 20%.
b. Imprima o total de livros analisados.
c. Imprima o preço médio de venda dos livros (com lucro de 20%).
d. Imprima o preço de venda dos livros mais barato e mais caro'''


CUSTO_POR_PAGINA = 0.03
CUSTO_FIXO = 4397.00
CUSTO_ENCADERNACAO = {
    "simples": 4.30,
    "especial": 7.80,
    "luxo": 10.50
}

def calcular_preco_minimo(num_paginas, tipo_encadernacao, num_copias):
    custo_encadernacao = CUSTO_ENCADERNACAO[tipo_encadernacao]
    custo_total = (CUSTO_FIXO + (num_paginas * CUSTO_POR_PAGINA) + custo_encadernacao) * num_copias
    preco_minimo = custo_total / num_copias
    return preco_minimo

def calcular_preco_venda(preco_minimo):
    return preco_minimo * 1.20

def main():
    livros = []
    
    while True:
        num_paginas = int(input("Digite o número de páginas do livro (ou '0' para finalizar): "))
        if num_paginas == 0:
            break
        tipo_encadernacao = input("Digite o tipo de encadernação (simples/especial/luxo): ").lower()
        num_copias = int(input("Digite o número de vendas previstas (número de cópias): "))
        
        preco_minimo = calcular_preco_minimo(num_paginas, tipo_encadernacao, num_copias)
        preco_venda = calcular_preco_venda(preco_minimo)
        
        livros.append({
            "num_paginas": num_paginas,
            "tipo_encadernacao": tipo_encadernacao,
            "num_copias": num_copias,
            "preco_minimo": preco_minimo,
            "preco_venda": preco_venda
        })
    
    total_livros = len(livros)
    total_preco_venda = sum(livro["preco_venda"] for livro in livros)
    preco_medio_venda = total_preco_venda / total_livros if total_livros > 0 else 0
    livro_mais_barato = min(livros, key=lambda x: x["preco_venda"], default=None)
    livro_mais_caro = max(livros, key=lambda x: x["preco_venda"], default=None)
    
    print(f"\nTotal de livros analisados: {total_livros}")
    print(f"Preço médio de venda dos livros (com lucro de 20%): R${preco_medio_venda:.2f}")
    
    if livro_mais_barato:
        print(f"Preço de venda do livro mais barato: R${livro_mais_barato['preco_venda']:.2f}")
    if livro_mais_caro:
        print(f"Preço de venda do livro mais caro: R${livro_mais_caro['preco_venda']:.2f}")

if __name__ == "__main__":
    main()

