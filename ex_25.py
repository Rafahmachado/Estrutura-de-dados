''' Foi realizada uma pesquisa de algumas características físicas da população de uma
certa região, a qual foram coletados os seguintes dados referentes a cada habitante
para serem analisados:

• Sexo.
• Cor dos olhos (azuis, verdes, castanhos).
• Cor dos cabelos (louros, castanhos, pretos).
• Idade.
Faça um programa que determine e escreva:
a. O total de entrevistados
b. O total de homens e o total de mulheres entrevistados
c. A maior e a menor idade do conjunto de habitantes;
d. A média de idade do conjunto de habitantes;
e. A percentagem de indivíduos de sexo feminino cuja idade está entre 18 e 35
anos inclusive e que tenham olhos verdes e cabelos louros.
O final do conjunto de habitantes é reconhecido pelo valor -1 para a idade'''

def main():
    total_entrevistados = 0
    total_homens = 0
    total_mulheres = 0
    idades = []
    mulheres_18_35_verdes_louros = 0
    total_mulheres_18_35 = 0

    while True:
        idade = int(input("Digite a idade do habitante (ou '-1' para finalizar): "))
        if idade == -1:
            break
        sexo = input("Digite o sexo do habitante (masculino/feminino): ").lower()
        cor_olhos = input("Digite a cor dos olhos do habitante (azuis/verdes/castanhos): ").lower()
        cor_cabelos = input("Digite a cor dos cabelos do habitante (louros/castanhos/pretos): ").lower()
        
        total_entrevistados += 1
        idades.append(idade)
        
        if sexo == "masculino":
            total_homens += 1
        elif sexo == "feminino":
            total_mulheres += 1
            if 18 <= idade <= 35:
                total_mulheres_18_35 += 1
                if cor_olhos == "verdes" and cor_cabelos == "louros":
                    mulheres_18_35_verdes_louros += 1

    if total_entrevistados > 0:
        maior_idade = max(idades)
        menor_idade = min(idades)
        media_idade = sum(idades) / total_entrevistados
        if total_mulheres_18_35 > 0:
            porcentagem_mulheres_18_35_verdes_louros = (mulheres_18_35_verdes_louros / total_mulheres_18_35) * 100
        else:
            porcentagem_mulheres_18_35_verdes_louros = 0
    else:
        maior_idade = menor_idade = media_idade = porcentagem_mulheres_18_35_verdes_louros = 0

    print(f"\nTotal de entrevistados: {total_entrevistados}")
    print(f"Total de homens: {total_homens}")
    print(f"Total de mulheres: {total_mulheres}")
    print(f"Maior idade: {maior_idade}")
    print(f"Menor idade: {menor_idade}")
    print(f"Média de idade: {media_idade:.2f}")
    print(f"Percentagem de mulheres entre 18 e 35 anos com olhos verdes e cabelos louros: {porcentagem_mulheres_18_35_verdes_louros:.2f}%")

if __name__ == "__main__":
    main()
