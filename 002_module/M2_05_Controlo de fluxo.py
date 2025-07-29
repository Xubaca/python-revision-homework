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
    somatario : int = int(input("De que numero é que quer fazer o somatorio?\n"))
    soma :int = somatario
    for i in range(0,somatario):
        soma += i
    print(f"O Resultadao e:\t{soma}")
    pass




#**3) Faça um programa que solicite ao utilizador 2 números e apresente as seguintes opções:**

#* Mostrar a soma dos dois números
#* Mostrar o resto dos dois números (o primeiro menos o segundo)
#* Mostrar a multiplicação dos dois números
#* Em caso de não introduzir uma opção válida, o programa irá informar que não é correta

def pergunta_3():
    numero_1: int = 0
    numero_2: int = 0
    while True:
        try:
            numero_1 = int(input("Primeiro numero:\t"))
            numero_2 = int(input("Segundo numero:\t"))
            break
        except:
            print("Por favor apenas numeros!")
    #defenicao das opcoes
    soma = lambda x,y: x+y
    resto = lambda x,y: x%y
    multiplicacao = lambda x,y: x*y
    while True:
        try:
            print("Por favor escolha uma opcao:\n\t1)-soma;\n\t2)-multiplicacao;\n\t3)-resto")
            resposta = int(input("Qual e a sua escolha?:\t"))
            #switch case
            match resposta:
                case 1:
                    print(soma(numero_1,numero_2))
                case 2:
                    print(multiplicacao(numero_1,numero_2))
                case 3:
                    print(resto(numero_1,numero_2))
                #error handling
                case _:
                    print("opcao Invalida!")
                    continue
            break
        #error handling
        except:
            print("Por favor apenas escolha, opcoes validas!")
    pass

def pergunta_4():
    #armazena todas as respostas
    respostas :list[int] = []
    #corre o loop ate um numero par ser introduzido
    while True:
        print("Que numero e que deseja intrudozir:\t")
        respostas.append(int(input("")))
        if respostas[-1] % 2 == 0: break
        else:
            print("Os numeros introduzidos!\n",respostas)

def pergunta_5():
    soma :int = 0
    #loop de 2 em 2
    for i in range(0,101,2):
        soma += i
        print(f"A soma atual: {soma}")

