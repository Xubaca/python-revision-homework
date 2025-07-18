###**1) Faça um programa que solicite ao utilizador três números individualmente e realize as seguintes verificações:**
#* Se os números estão por ordem ascendente ou decrescente
#* Se há um erro devido a que o primeiro número introduzido é 0

def pergunta_1():
    numeros :list = []
    #um while para ser possivel repetir respostas caso ocorra o erro do 0
    iterator :int = 0
    while iterator<3:
        resposta = int(input("Digite os numeros: "))
        #vaildação se o primeiro numero é de facto 0
        if(len(numeros) == 0 and resposta == 0):
            print("O primeiro numero não pode ser 0!")
        #append
        else:
            iterator += 1
            numeros.append(resposta)
        print(numeros)

    #+=1 se o numero é menor que o seguinte ou -=1
    order :int = 0
    #vira true se houver numeros iguais
    equal_counter :bool = False
    for i in range(0,2):
        if(numeros[i] >  numeros[i+1]):
            order += 1
        elif(numeros[i] < numeros[i+1]):
            order -= 1
        else:
            equal_counter = True

    #Controla a resposta se houver um numero igual
    if(equal_counter):
        match order:
            case 2:
                print("Ordem ascendente!\n")
            case -2:
                print("Ordem Descnedente!\n")
            case _:
                print("Nenhuma ordem!")
    #Controla se não houver numeros iguais
    else:
        match order:
            case 3:
                print("Ordem ascendente!\n")
            case -3:
                print("Ordem descendente!\n")
            case _:
                print("NEnhuma Ordem!\n")



pergunta_1()