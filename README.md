Autor: Rodrigo Amaral de Castro Valente

## Objetivo do programa

 Verificar se carga da bateria de um robô é suficiente para durar uma dada missão. O usuário informa a % atual da bateria, o tempo estimado da missão em minuto e o consumo percentual por minuto. Com esses dados, o programa calcula o consumo total e informa ao usuário a viabilidade, quanto sobra de carga ou quanto falta.


## Requisitos

- Python 3.6 ou superior

## Comando para executar o programa

Abra o terminal na pasta principal do repositório e execute:

python3 src/missao.py


## Exemplo de entrada 1 (missão viavel):
```
Digite o valor atual da bateria em porcentagem : 80
Digite o tempo estimado de missão, em minutos: 30
Digite quantos porcento a bateria é consumida por minuto: 2
```

**Saída:**
```
--------------------------------
| A MISSÃO PODE SER CONCLUIDA |
--------------------------------
Bateria Restante: 20.0%
```

### Exemplo de entrada 2 (missão inviável):
```
Digite o valor atual da bateria em porcentagem : 50
Digite o tempo estimado de missão, em minutos: 40
Digite quantos porcento a bateria é consumida por minuto: 2
```

**Saída:**
```
--------------------------------
| A MISSÃO NÂO PODE SER CONCLUIDA |
--------------------------------
faltará: 30.0% de bateria
```

### Exemplo de entrada 3 (input inválido): 
```
Digite o valor atual da bateria em porcentagem : 150
```

**Saída:**
```
Valor Invalido! Encerrando o programa...
```