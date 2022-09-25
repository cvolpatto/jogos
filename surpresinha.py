import random
import re
from tkinter import END, N
import streamlit as st

#st.title('Escolha o jogo desejado') # no meio da tela

op = st.sidebar.selectbox("Escolha o jogo",("1 - mega-sena","2 - lotofácil","3 - quina"))

if op == "2 - lotofácil":
    st.write("Digite a quantidade de 6 à 15 números:")
    st.text_area("Digite seu texto aqui")

    button = st.button("clique aqui")



#numero = st.debar.number_input("numero", value=1,max_value=10, min_value=0)
#slider = st.sidebar.slider("meu texto", 50, 90 , 70)
"""

#st.selectbox("Escolha o jogo",("1 - mega-sena","2 - lotofácil","3 - quina"))
print ("Digite o numero do jogo: \n")
print("1 - mega-sena")
print("2 - lotofácil")
print("3 - quina")
print("4 - lotomania")
print("5 - timemania")
print("6 - dupla sena")     
print("7 - dia de sorte")
#print("8 - supersete")
print("9 - +milionaria")

minimo_megasena = int(1)
maximo_megasena = int(61)
minimo_lotofacil = int(1)
maximo_lotofacil = int(26)
minimo_quina = int(1)
maximo_quina = int(61)
minimo_lotomania = int(1)
maximo_lotomania = int(101)
minimo_timemania = int(1)
maximo_timemania = int(81)
minimo_duplasena = int(1)
maximo_duplasena = int(51)
minimo_diadesorte = int(1)
maximo_diadesorte = int(32)
minimo_supersete = int(7)
maximo_supersete = int(21)
minimo_milionaria = int(1)
maximo_milionaria = int(51)

arrary_jogos = []
indice_jogos = int(0)
indice_numeros = int(0)

jogo = int(input("Digite o numero do jogo desejado: "))

if jogo == 1:
    qtd_jogos = int(input("Digite a quantidade de jogos da mega-sena: "))
    qtd_numeros =int(input("Digite a quantidade de 6 à 15 números: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_megasena, maximo_megasena)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_megasena, maximo_megasena))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))
END


if jogo == 2:
    qtd_jogos = int(input("Digite a quantidade de jogos da lotofácil: "))
    qtd_numeros =int(input("Digite a quantidade de 15 à 18 números: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_lotofacil, maximo_lotofacil)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_lotofacil, maximo_lotofacil))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))
END

if jogo == 3:
    qtd_jogos = int(input("Digite a quantidade de jogos da quina: "))
    qtd_numeros =int(input("Digite a quantidade de 5 à 15 números: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_quina, maximo_quina)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_quina, maximo_quina))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))

END

if jogo == 4:
    qtd_jogos = int(input("Digite a quantidade de jogos da lotomania: "))
    qtd_numeros = 50 #int(input("Digite a quantidade de 50 numeros: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_lotomania, maximo_lotomania)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_lotomania, maximo_lotomania))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))
END

if jogo == 5:
    qtd_jogos = int(input("Digite a quantidade de jogos da timemania: "))
    qtd_numeros = 10 #int(input("Digite a quantidade de 10 numeros: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_timemania, maximo_timemania)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_timemania, maximo_timemania))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))
    times = ['ABC/RN','ALTOS/PI','AMERICA/MG','AMERICA/RN','APARECIDENSE/GO','ATHLETICO/PR','ATLETICO/AC',
    'ATLETICO/CE','ATLETICO/GO','ATLETICO/MG','AVAI/SC','BAHIA/BA','BOA ESPORTE/MG','BOAVISTA/RJ','BOTAFOGO/PB',
    'BOTAFOGO/RJ','BOTAFOGO/SP','BRAGANTINO/SP','BRASIL/RS','BRASILIENSE/DF','BRUSQUE/SC','CAMPINENSE/PB',
    'CAXIAS/RS','CHAPECOENSE/SC','CIANORTE/PR','CONFIANCA/SE','CORINTHIANS/SP','CORITIBA/PR','CRB/AL','CRICIUMA/SC',
    'CRUZEIRO/MG','CSA/AL','CUIBA/MT','FERROVIARIO/SP','FERROVIARIO/CE','FIGUEIRENSE/SC','FLAMENGO/RJ',
    'FLORESTA/CE','FLUMINENSE/RJ','FORTALEZA/CE','GOIAS/GO','GREMIO/RS','GUARANI/SP','IMPERATRIZ/MA','INTERNACIONAL/RS',
    'ITUANO/SP','JACUIPENSE/BA','JOINVILLE/SC','JUAZEIRENSE/BA','JUVENTUDE/RS','LONDRINA/PR','LUVERDENSE/MT','MANAUS/AM',
    'MIRASOL/SP','MOTOCLUB/MA','NAUTICO/PE','NOVORIZONTINO/SP','OESTE/SP','OPERARIO/PR','PALMEIRAS/SP','PARANA/PR',
    'PAYSANDU/PA','PONTE PRETA/SP','REMO/PA','SAMP CORREA/MA','SANTA CRUZ/PE','SANTOS/SP','SAO BENTO/SP','SAO JOSE/RS'
    'SAO PAULO/SP','SAORAIMUNDO/RR','SPORT/PE','TOMBENSE/MG','TREZE/PB','VASCO DA GAMA/RJ','VILA NOVA/GO','VITORIA/BA',
    'VOLTA REDONDA/RJ','YPIRANGA/RS']
    def selectRandom(times):
        return random.choice(times)
    print("O Time escolhido é: ", selectRandom(times))
END

if jogo == 6:
    qtd_jogos = int(input("Digite a quantidade de jogos da duplasena: "))
    qtd_numeros = int(input("Digite a quantidade de 50 numeros: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_duplasena, maximo_duplasena)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_duplasena, maximo_duplasena))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))
END

if jogo == 7:
    qtd_jogos = int(input("Digite a quantidade de jogos Dia de Sorte: "))
    qtd_numeros = int(input("Digite a quantidade de 7 à 15 numeros: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_diadesorte, maximo_diadesorte)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_diadesorte, maximo_diadesorte))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))
    meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto',
    'setembro','outubro','novembro','dezembro']
    def selectRandom(meses):
        return random.choice(meses)
    print("O mês escolhido é: ", selectRandom(meses))
END

if jogo == 8:
    qtd_jogos = int(input("Digite a quantidade de jogos da Super 7 : "))
    qtd_numeros = int(input("Digite a quantidade de 7 à 21 numeros: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_duplasena, maximo_duplasena)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_duplasena, maximo_duplasena))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))

    def select_random_Ns(lst, n):
        random.shuffle(lst)
        result = []
        for i in range(0, len(lst), n):
            result.append(lst[i:i + n])
            return result
     
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(select_random_Ns(lst, 2))

END

if jogo == 9:
    qtd_jogos = int(input("Digite a quantidade de jogos da +milionária : "))
    qtd_numeros = int(input("Digite a quantidade de 6 à 12 numeros: "))
    for indice_jogos in range(qtd_jogos):
            array_jogos = []
            for indice_numeros in range(qtd_numeros):
                numero_sorteado = random.randrange(minimo_milionaria, maximo_milionaria)
                while numero_sorteado in array_jogos:
                    numero_sorteado = int(random.randrange(minimo_milionaria, maximo_milionaria))
                array_jogos.append(numero_sorteado)
                strs = (array_jogos)
                strs.sort()
            print("jogo" + str(indice_jogos+1) + ": " + str(strs))
    trevo = [1,2,3,4,5,6]
    def selectRandom(trevo):
        return random.choice(trevo)
    print("O mês escolhido é: ", random.sample(trevo,2))

END

"""