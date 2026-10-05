# % atual da bateria
bateria_inicial = 0

#tempo estimado de da duração da missão (Em minutos)
tempo_missao = 0

#consumo por minuto em %
consumo = 0

#coleta dos dados reais
bateria_inicial= float(input("Digite o valor atual da bateria em porcentagem : "))
tempo_missao = float(input("Digite o tempo estimado de missão, em minutos: "))
consumo = float(input("Digite quantos porcento a bateria é consumida por minuto: "))

#calculo de quanto será consumido e quanto de bateria terá no fim
consumo_total = tempo_missao * consumo
bateria_fim = bateria_inicial - consumo_total
if consumo_total <= bateria_inicial:
    print("--------------------------------")
    print("| A MISSÃO PODE SER CONCLUIDA |")
    print("--------------------------------")
    print(f"Bateria Restante: {bateria_fim}% \n")
elif consumo_total > bateria_inicial:
    print("--------------------------------")
    print("| A MISSÃO NÂO PODE SER CONCLUIDA |")
    print("--------------------------------")
    print(f"faltará: {bateria_fim}% de bateria\n")
#print(f"O consumo total foi de : {consumo_total} \nBateria ao fim: {bateria_fim} ")