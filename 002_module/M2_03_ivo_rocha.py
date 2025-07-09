from os import remove


def pergunta_1():
    #defenicao das variaveis
    lol_champs_list :list[str] = ["Garen","Katarina","Ashe","Warwick"]
    lol_champs_tuple :tuple[str, str, str, str] = ("Nami","Soraka","Miss Fortune","Lucian")
    #prints
    print(lol_champs_list)
    print(lol_champs_tuple)
    #index print
    print(lol_champs_list[1] + " " + lol_champs_tuple[-1])
    #modificao e print
    #tuple
    #é imutavel por isso tem que se fazer assim ou via pointers
    temp_list = list(lol_champs_tuple)
    temp_list[0] = "Lee sin"
    lol_champs_tuple = tuple(temp_list)
    print(lol_champs_tuple)
    #listas são mutaveis
    lol_champs_list[0] = "Rengar"
    print(lol_champs_list)
    #print dos tamanhos
    print(f"O tamanho da lista é {len(lol_champs_list)}")
    print(f"O tamanho do tuple é {len(lol_champs_tuple)}")
    #adicao e print
    temp_list = list(lol_champs_tuple)
    temp_list.append("Aatrox")
    lol_champs_tuple = tuple(temp_list)
    print(lol_champs_tuple)
    lol_champs_list.append("Bard")
    print(lol_champs_list)
    #apagar e print
    temp_list=list(lol_champs_tuple)
    temp_list.remove("Aatrox")
    lol_champs_tuple = tuple(temp_list)
    print(lol_champs_tuple)
    lol_champs_list.remove("Bard")
    print(lol_champs_list)

#**2) Trabalhar com sets e dicionários**

#* Crie um set com pelo menos 3 elementos relacionados a um tema (por exemplo: veículos, comida, música).
#* Crie um dicionário com 3 pares chave-valor relacionados ao mesmo tema.
#* Mostre o set e o dicionário.
#* Mostre o 2º elemento do set e o valor da primeira chave-valor do dicionário.
#* Modifique um elemento do set ou do dicionário e mostre o resultado.
#* Mostre o tamanho do set e do dicionário.
#* Pesquise se um elemento está presente no set e no dicionário e mostre os resultados (True ou False).
#* Adicione um elemento ao set e uma chave-valor ao dicionário e mostre ambos.
#* Apague o conteúdo do set e do dicionário e mostre-os novamente.
def pergunta_2():
    #instanciacao
    #ordem dos meus favoritos
    one_piece_set :set[str] = {"usopp","zoro","Dr. chopper"}
    #ordem de chegada à crew
    one_piece_dict :dict[int:str] = {
        0:"luffy",
        1:"zoro",
        2:"Nami"
    }
    print(one_piece_set)
    print(one_piece_dict)
    print(type(one_piece_set))
    #printing das estruturas
    temp_list_one_piece:list = list(one_piece_set)
    print(temp_list_one_piece[1])
    print(next(iter(one_piece_dict.values())))
    #modificação
    one_piece_dict[2] = "Sanji"
    print(one_piece_dict)
    #printing size
    print(len(one_piece_dict))
    print(len(one_piece_set))

    #pesquisa de elementos

    resp :str = input("Que elemento é que quer pesquisar nas duas estruturas?")
    print("O dict tem este valor?\t" + str(resp in one_piece_dict.values()))
    print("O set tem este valor?\t" + str(resp in one_piece_set))

    #adicao de elementos
    one_piece_dict[4] = "Nami"
    one_piece_set.add("Sniper King")
    print(one_piece_dict)
    print(one_piece_set)

    #apagar o conteudo
    one_piece_dict.clear()
    one_piece_set.clear()
    print(one_piece_dict)
    print(one_piece_set)


#**3) Peça ao utilizador para inserir 3 números (inteiros ou decimais) individualmente.**
#* Crie uma lista com os números fornecidos.
#* Calcule o somatório dos elementos da lista.
#* Imprima o resultado.
#*Ajuda: existe uma função chamada sum(lista) Experimente-a!*
def pergunta_3():
    numeros:list = []
    i:int = 0
    while(i < 3):
        try:
            #podemos sempre guardar ints como floats por isso é mais facil se assumirmos sempre que são floats
            dynamic_variable = (float)(input("Por favor insira um numero! apenas ints ou floats!\n"))
            numeros.append(dynamic_variable)
            i+=1
        except:
            print("Por favor apenas ints e floats")
    soma :float = sum(numeros)
    print(f"A soma é:\t{round(soma,2)}")

#**4) Peça ao utilizador para inserir 4 números (inteiros ou decimais) individualmente.**
#* Crie uma lista com os números fornecidos.
#* Calcule a média aritmética dos elementos da lista.
#* Imprima o resultado.
#*Neste caso sabemos que o número de elementos que o utilizador introduziu é 4, mas o objetivo será deixar o programa abstrato,e portanto,
#não fazer referência ao número 3; deve calcular o numeros de elementos da lista*
def pergunta_4():
    numeros:list =[]
    i :int = 0
    while(i<3):
        try:
            #inteiros e floats podem ser guardados dentro de um float
            resposta:float = (float)(input("Por favor digite o numero desejado!\n"))
            numeros.append(resposta)
            i+=1
        except:
            print("Por favor, apenas numeros")
    #usamos o sum falado na pergunta anterior para facilitar o calculo ,não tendo de fazer um for loop
    media :float = sum(numeros)/4
    print(f"A soma é {round(media,2)}")

    #**5) Crie uma matriz inicial com quatro sublistas, cada uma contendo três números inteiros.**
    #* Calcule a soma dos três primeiros elementos da primeira sublista e adicione esse resultado como o quarto elemento na mesma sublista.
    #* Repita o processo para as outras três sublistas, calculando a soma dos três primeiros elementos e adicionando esse resultado como o quarto elemento em cada sublista.
    #*Não vale colocar diretamente os valores (nem os índices nem a soma)
    #*Há que pesquisar uma forma automatizada de aceder e modificar esses valores

def pergunta_5():
    matriz :list[list[int]] = [
        [1, 1, 1],
        [2, 2, 7],
        [3, 3, 9],
        [4, 4, 13]
    ]
    #usando a funcao Sum conseguimos obter o resultado sem necessitar de um ciclo for ou foreach
    matriz[0].append(sum(matriz[0]))
    print(matriz[0])
    #iteração para evitar repetição de código
    # Eu acho que isto satisfas a condição "Não vale colocar diretamente os valores (nem os índices nem a soma)"
    for i in range(1,4):
        matriz[i].append(sum(matriz[i]))
    print(matriz)
    pass


def pergunta_6():
    cavaleiro = {'vida': 2, 'ataque': 2, 'defesa': 2, 'alcance': 2}
    guerreiro = {'vida': 2, 'ataque': 2, 'defesa': 2, 'alcance': 2}
    arqueiro = {'vida': 2, 'ataque': 2, 'defesa': 2, 'alcance': 2}
    

    pass


pergunta_5()