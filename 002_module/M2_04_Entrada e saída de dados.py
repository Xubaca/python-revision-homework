#**1) Utilizar o método input() para fazer as seguintes tarefas:**
#* Peça um número ao utilizador e imprima o resultado juntamente com o tipo de dado capturado pela função input().
#* Peça um número ao utilizador e converta o valor introduzido para o formato int. Em seguida, imprima o número inteiro e o seu tipo.
#* Peça um número ao utilizador e converta o valor introduzido para o formato float. Imprima o número decimal e o seu tipo.
def pergunta_1():
    #declaração
    user_input = input("Por favor introduza um numero:\t")
    #printing
    print(user_input + f" que é do tipo {type(user_input)}")

    #segundo problema
    while True:
        #Para garantir a introdução de um int
        try:
            answer :int = int(input("Por favor digite um numero(formato int)!\n"))
            print(f"O numero escolhido foi {answer} e o seu tipo é {type(answer)}")
            break
        except:
            print("Por favor apenas numeros!")

    #loop de respostas
    while True:
        try:
            #validação da resposta
            second_answer:float = float(input("Por favor digite um numero(formato float)!\t"))
            print(f"VOce escolheu o seguinte numero {second_answer} e é do tipo {type(second_answer)}")
            #exit do loop
            break
        except:
            print("Por favor apenas numeros!")

    pass

###**2) Formatar os seguintes valores para mostrar o resultado indicado (deve usar o método format()):**
#* “Olá Mundo” → Alinhado à direita em 20 caracteres
#* “Olá Mundo” → Truncagem no quarto carácter (usar índice 3)
#* “Olá Mundo” → Alinhamento ao centro em 20 caracteres com truncagem no segundo carácter (usar índice 1)
#* 150 → Formatar com 5 números inteiros preenchidos com zeros
#* 7887 → Formatar com 7 números inteiros preenchidos com espaços
#* 20.02 → Formatar com 3 números inteiros e 3 números decimais

def pergutna_2():
    
    pass