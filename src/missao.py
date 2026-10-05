import sys 
#----------------------------------------------
#Declaração inicial das variaveis iniciais
bateria_inicial = 0 #Em %
tempo_missao = 0 #Em min
consumo = 0 #Em %/min
#---------------------------------------------


#-------------------------------------------------------------------------------------------
#coleta dos dados reais: bateria_inicial em (%), tempo_missão em (min), consumo em (%/min)
bateria_inicial= float(input("Digite o valor atual da bateria em porcentagem : "))
if  bateria_inicial < 0 or bateria_inicial >100:
    sys.exit("\nValor Invalido! Encerrando o programa...\n")

tempo_missao = float(input("Digite o tempo estimado de missão, em minutos: "))
if tempo_missao <= 0:
    sys.exit("\nValor Invalido! Encerrando o programa...\n")

consumo = float(input("Digite quantos porcento a bateria é consumida por minuto: "))
if consumo <= 0:
    sys.exit("\nValor Invalido! Encerrando o programa...\n")
#--------------------------------------------------------------------------------------


#------------------------------------------------------------------
#calculo de quanto será consumido e quanto de bateria terá no fim
consumo_total = tempo_missao * consumo
bateria_fim = bateria_inicial - consumo_total
#------------------------------------------------------------------

#-------------------------------------------------------------------
#resultados Finais do programa
if consumo_total <= bateria_inicial:
    print("\n--------------------------------")
    print("| A MISSÃO PODE SER CONCLUIDA |")
    print("--------------------------------")
    print(f"Bateria Restante: {bateria_fim}% \n")

elif consumo_total > bateria_inicial:
    print("\n--------------------------------")
    print("| A MISSÃO NÂO PODE SER CONCLUIDA |")
    print("--------------------------------")
    print(f"faltará: {abs(bateria_fim)}% de bateria\n")
#-------------------------------------------------------------------