#Autor: Daniel Birenbaum Guerrieri de Castro
#Github: https://github.com/danielbirenbaum






print("Programa que verifica bateria do robô, insira os valores desejados:")
print("OBS: Use números flutuantes, não digite (%) nem dimensões")

try:
    bateriaAtual = float(input("Digite o valor da bateria atualmente (%): "))
    duracaoPrevista = float(input("Digite a duração prevista da missão: "))
    consumo = float(input("Indique o consumo da bateria, em pontos percentuais: "))
    
except ValueError:
    print("Valores incompatíveis, encerrando o programa.")
    