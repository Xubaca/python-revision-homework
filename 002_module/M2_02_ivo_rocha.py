
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
