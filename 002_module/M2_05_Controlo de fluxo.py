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
    for i in range(0,2):
        if(numeros[i] >  numeros[i+1]):
            order -= 1
        else:
            order += 1

    #Controla o output
    match order:
        case 2:
            print("Ordem ascendente!\n")
        case -2:
            print("Ordem descendente!\n")
        case _:
            print("NEnhuma Ordem!\n")



def pergunta_2():

    pass