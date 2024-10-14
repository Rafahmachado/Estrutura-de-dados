'''Um dado material radioativo perde metade de sua massa a cada 50s. Dada a massa
inicial em gramas, fazer um algoritmo que determine o tempo necessário para que
essa massa seja menor que 0,5g.'''



# algoritmo 
# Função :Calcular o tempo para a massa atingir 0.5

# var
#  tempo,contador,massainicial,massa:real  //aqui você declara suas variaveis  !!
# inicio
#    escreva("digite a massa inicial em gramas:") //aqui você informa o que o usuario tem que fazer !!!
#    leia(massa)  // aqui vai ler a massa
#    massainicial<-massa // massa inicial recebe o valor d massa pra guardar e escrever no final do algoritmo informando ao usuario
# enquanto (massa>=0.5) faca //aqui ele faz o loop enquanto a massa não atingir o valor de 0.5
#        massa<-massa/2
#        contador <- contador+1 // ele conta o numero d vezes q a massa foi dividida
#        tempo<-contador*50 // pra descobrir o tempo q foi gasto ele multiplica o contador por 50 pra achar o tempo total
#      fimenquanto
#  escreval ("Massa inicial: ", massainicial)
#  escreval("Tempo calculado em segundos: ",tempo)
# fimalgoritmo

# Função: Calcular o tempo para a massa atingir 0.5 gramas

# Declaração das variáveis
tempo = 0
contador = 0
massainicial = 0
massa = 0

# Solicita ao usuário para digitar a massa inicial em gramas
massa = float(input("Digite a massa inicial em gramas: "))

# Armazena a massa inicial para exibir no final
massainicial = massa

# Loop que continua enquanto a massa for maior ou igual a 0.5 gramas
while massa >= 0.5:
    massa = massa / 2  # Divide a massa por 2
    contador += 1  # Incrementa o contador de divisões
    tempo = contador * 50  # Calcula o tempo total em segundos

# Exibe a massa inicial e o tempo calculado
print("Massa inicial:", massainicial)
print("Tempo calculado em segundos:", tempo)

	

 

