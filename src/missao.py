# % atual da bateria
bat_atual = 0

#tempo estimado de da duração da missão (Em minutos)
tempo_missao = 0

#consumo por minuto em %
consumo = 0

#coleta dos dados reais
bat_atual= float(input("Digite o valor da porcentagem atual da bateria: "))
tempo_missao = float(input("Digite quantos minutos a missão está estimada: "))
consumo = float(input("Digite o valor de quantos porcento a bateria é consumida por minuto: "))

#calculo de quanto será consumido e quanto de bateria terá no fim
consumo_total = tempo_missao * consumo
bat_fim = bat_atual - consumo_total


print(f"O consumo total foi de : {consumo_total} \nBateria ao fim: {bat_fim} ")