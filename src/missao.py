#Autor: Daniel Birenbaum Guerrieri de Castro
#Github: https://github.com/danielbirenbaum

#Função que calcula consumo total do robô
def calculoConsumo(duracaoPrevista, consumo):
    return duracaoPrevista*consumo

#Função que define se é possível terminar a missão
def avaliaConsumo(bateriaAtual,consumoTotal):
    return True if (bateriaAtual >= consumoTotal) else False

#Calcula a bateria restante após possível consumo total da missão
def bateriaRestante(bateriaAtual,consumoTotal):
    return bateriaAtual - consumoTotal

#Programa principal, toma input do usuário e verifica para possíveis excessões de tipo
print("\033[1;34mPrograma que verifica bateria do robô, insira os valores desejados:\033[0m")


try:
    bateriaAtual = float(input("Digite o valor da bateria atualmente (%): "))
    duracaoPrevista = float(input("Digite a duração prevista da missão: "))
    consumo = float(input("Indique o consumo da bateria, em pontos percentuais: "))
    
    #Verificação de valores da bateria, consumo e duração
    bateriaOk = True if (bateriaAtual>= 0 and bateriaAtual <= 100) else False
    duracaoOk = True if duracaoPrevista >= 0 else False
    consumoOk = True if consumo >= 0 else False
    
    if (not(bateriaOk and duracaoOk and consumoOk)):
        print("\033[91mValor inválido! Verificar se os valores inseridos estão corretos\033[0m")
    else:
        consumoTotal = calculoConsumo(duracaoPrevista, consumo)
        conclusaoPossivel = avaliaConsumo(bateriaAtual, consumoTotal)
        if (conclusaoPossivel and bateriaOk and duracaoOk and consumoOk):       
            print("A missão \033[1;34mpode\033[0m ser concluída!")
            print(f"Bateria restante após término da missão: \033[1;34m{bateriaRestante(bateriaAtual, consumoTotal)}%\033[0m")
        else:
            print("A missão \033[91mNÃO pode\033[0m ser concluída!")
            print(f"A bateria necessária para concluir a missão seria de: \033[91m{(-1)*bateriaRestante(bateriaAtual, consumoTotal)}%\033[0m")
              
       
except ValueError:
    print("\033[91mERRO: Valores incompatíveis, encerrando o programa.\033[0m")
    
except ArithmeticError:
    print("\033[91mERRO: Problema ao realizar calculo requisitado, encerrando o programa.\033[0m")

    