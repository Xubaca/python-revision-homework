
def main():
    # Use a breakpoint in the code line below to debug your script.
    first :float = 5.0
    second :float = 6.0
    third :float = 7.0
    #printing the average
    print(f"a nota média é {(first + second + third)/3}")

    primeira_nota :float = 15.0
    segunda_nota :float = 14.0
    terceira_nota :float = 12.0
    quarta_nota :float = 19.0

    #calculo
    media :float = primeira_nota*.15 + segunda_nota*.35 + terceira_nota*.20 + quarta_nota*.30
    print("A média é :\t"+ str(media))

    primeiro_valor :int = int(input("Primeiro valor: "))
    segundo_valor :int = int(input("Segundo valor: "))

    #perguntas:
    #1 pergunta
    #operador ternário para simplificar sintax
    print("Os numeros são iguais:\t" + str(primeiro_valor==segundo_valor))#True if primeiro_valor == segundo_valor else False )
    #2 pergunta
    print( "Os numeros são diferentes:\t"+ str(primeiro_valor!=segundo_valor))#False if segundo_valor == primeiro_valor else True )
    #3 pergunta
    print("O primeiro numero é maior?\t" + str(primeiro_valor>segundo_valor))#True if primeiro_valor > segundo_valor else False )
    #4 pergunta
    print("O segundo numero é maior?\t" + str(segundo_valor>primeiro_valor))

    #pedido de input
    user_input :str = input("digite qq coisa:\t")

    #print da resposta
    print(True if 3 <= len(user_input) < 10 else False)

    #declaracao das variaveis
    numero_magico :int = 12345679
    multiplicador:int = 0
    #garantir que apenas aceitamos ints
    while(True):
        try:
            multiplicador = (int)(input("Por favor insira um numero entre 1 e 9").strip())
            if 0 < multiplicador < 10:  break
        except:
            print("Por favvor apenas numeros de 1 a 9")
    #calculos
    numero_utilizador :int = 9 * multiplicador
    numero_magico = numero_utilizador * numero_magico
    #prints
    print(f"O novo numero e {numero_magico}")




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
