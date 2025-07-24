###**1) Faça um programa que solicite ao utilizador três números individualmente e realize as seguintes verificações:**
#* Se os números estão por ordem ascendente ou decrescente
#* Se há um erro devido a que o primeiro número introduzido é 0
from os.path import pardir


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
    numero :int = int(input("Por favor diga-me que numero é que quer fazer o somatório!"))
    #iteration:
    for i in range(1,numero): numero+=i
    print(numero)
    pass

###**3) Faça um programa que solicite ao utilizador 2 números e apresente as seguintes opções:**

#* Mostrar a soma dos dois números
#* Mostrar o resto dos dois números (o primeiro menos o segundo)
#* Mostrar a multiplicação dos dois números
#* Em caso de não introduzir uma opção válida, o programa irá informar que não é correta

def pergunta_3():
    #instanciação
    numero_1: int
    numero_2: int
    while True:
        #como não existe um tryparse é ncessário fazer um try catch
        try:
            numero_1 = int(input("Digite o primeiro numero:\t"))
            numero_2 = int(input("Digite o segundo numero:\t"))
            break
        except:
            print("por favor apenas numeros!\n")
    #realização das operações
    soma = lambda a,b: a+b
    resto = lambda a,b: a%b
    mult = lambda a,b: a*b

    print(f"A Soma dos dois numeros é:\t{soma(numero_1, numero_2)}\nO resto da Divisão dos dois numeros é:\t{resto(numero_1, numero_2)}\nA multiplicaçãod dos dois numeros é:\t{mult(numero_1, numero_2)}\n")
    pass


#**4)  Faça um programa que solicite ao utilizador que introduza um número e o apresente.**
#* Repita o processo enquanto o utilizador continuar a introduzir números ímpares.
#* Quando o utilizador introduzir um número par, pare o programa.

def pergunta_4():
    while True:
        respostas:list = []
        try:
            numero:int =int(input("Que"))
    pass