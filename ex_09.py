''' Em um sistema de ensino experimental em 10 níveis, o aluno é submetido a 
exercícios sobre o mesmo assunto até que ele alcance a nota máxima (100 pontos), 
para só então passar ao assunto seguinte. 
Entretanto, se após 5 tentativas no mesmo  nível o aluno obtiver menos de 300 pontos acumulados 
ele retorna ao nível anterior. Caso contrário, ele permanece no mesmo nível, zerando novamente os 
pontos acumulados.

Faça um programa que compute o progresso do aluno, através da leitura de suas notas até que ele 
termine o 10º nível. Utilize o comando break(por exemplo, para passar ao próximo nível e recomeçar
 quando o aluno tiver tirado a nota máxima).'''

# Definindo nível inicial,tentativas e pontos acumulados 
nivel = 1
tentativas = 0
pontos_acumulados = 0
#loop que vai controlar o progresso do aluno através dosa níveis,continua até completar nível 10
while nivel <= 10:
    print(f"Nível {nivel}")
 #loop tentativas,dentro de cada nível,um loop for permite até 5 tentativas    
    for _ in range(5):
        #Solicita a nota do aluno
        nota = int(input("Digite a nota do aluno (0 a 100): "))
        pontos_acumulados += nota #Adiciona a nota aos pontos acumulados
        tentativas += 1 #Incrementa o contador  de tentativas 

#Se a nota máxima for alcançada,passa para o proxímo nivel

        if nota == 100:
            print("Nota máxima alcançada! Passando para o próximo nível.")
            nivel += 1 # próximo nível
            tentativas = 0 # zera o contador de tentativas 
            pontos_acumulados = 0 # Zera os pontos acumulados
            break # Sai do loop de tentativas para passar ao próximo nível
# Verifica se o aluno completou as 5 tentaivas 
    if tentativas == 5:
        if pontos_acumulados < 300: # Veriica se os pontos são insuficientes
            print("Pontos insuficientes. Retornando ao nível anterior.")
            nivel = max(1, nivel - 1) # Retorna ao nível anterior
        else:
            print(" Não alcançou a nota máxima, permanece no mesmo nível.")
        tentativas = 0
        pontos_acumulados = 0

print("Parabéns! Você completou todos os níveis.")


