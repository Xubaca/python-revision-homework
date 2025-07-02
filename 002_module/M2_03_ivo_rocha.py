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


def pergunta_2():
    #instanciacao
    one_piece_set :set[str] = {"luffy","zoro","Dr. chopper"}
    #ordem de chegada à crew
    one_pice_dict :dict[int:str] = {
        1:"luffy",
        2:"zoro",
        3:"Nami"
    }
    print(one_piece_set)
    print(one_pice_dict)
    print()



pergunta_2()