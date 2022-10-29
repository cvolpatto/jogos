from cgitb import text
import random
import re
from selectors import SelectSelector
from click import option
from jinja2 import select_autoescape
import streamlit as st
from random import randint
import numpy as np
import locale

st.title('Gerador de Jogos para Loterias Caixa')

arrary_jogos = []
indice_jogos = int(0)
indice_numeros = int(0)
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

op = st.selectbox("Escolha o jogo",("SELECIONE","1 - mega-sena","2 - lotofácil","3 - quina","4 - lotomania",
"5 - timemania","6 - dupla sena","7 - dia de sorte","8 - +milionaria"))

if op == "1 - mega-sena":
        qtd_jogos = st.number_input("Digite a quantidade de jogos da mega-sena:", max_value=100, min_value=1)
        qtd_numeros = st.number_input("Digite a quantidade de 6 à 15 números:", max_value=15, min_value=6)
        
        button = st.button("Confirmar")

        if button:
            if qtd_numeros == 6: 
                valor = 4.50 
            if qtd_numeros == 7:
                valor = 31.50
            if qtd_numeros == 8:
                valor = 126
            if qtd_numeros == 9:
                valor = 378
            if qtd_numeros == 10:
                valor = 945
            if qtd_numeros == 11:
                valor = 2079
            if qtd_numeros == 12:
                valor = 4158
            if qtd_numeros == 13:
                valor = 7722
            if qtd_numeros == 14:
                valor = 13513.50
            if qtd_numeros  == 15:
                valor = 22522.50
            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')

            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_megasena, maximo_megasena)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_megasena, maximo_megasena))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))

if op == "2 - lotofácil":
        qtd_jogos = st.number_input("Digite a quantidade de jogos da lotofácil:", max_value=200, min_value=1)
        qtd_numeros = st.number_input("Digite a quantidade de  15 à 20 números:", max_value=20, min_value=15)
        
        button = st.button("Confirmar")

        if button:
            if qtd_numeros == 15: 
                valor = 2.50 
            if qtd_numeros == 16:
                valor = 40
            if qtd_numeros == 17:
                valor = 340
            if qtd_numeros == 18:
                valor = 2040
            if qtd_numeros == 19:
                valor = 9690
            if qtd_numeros == 20:
                valor = 38760
            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')

            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_lotofacil, maximo_lotofacil)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_lotofacil, maximo_lotofacil))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))

if op == "3 - quina":
        qtd_jogos = st.number_input("Digite a quantidade de jogos da quina:", max_value=200, min_value=1)
        qtd_numeros = st.number_input("Digite a quantidade de 5 à 15 números:", max_value=15, min_value=5)
        
        button = st.button("Confirmar")

        if button:
            
            if qtd_numeros == 5: 
                valor = 2 
            if qtd_numeros == 2:
                valor = 12
            if qtd_numeros == 7:
                valor = 42
            if qtd_numeros == 8:
                valor = 112
            if qtd_numeros == 9:
                valor = 252
            if qtd_numeros == 10:
                valor = 504
            if qtd_numeros == 11:
                valor = 924
            if qtd_numeros == 12:
                valor = 1584
            if qtd_numeros == 13:
                valor = 2574
            if qtd_numeros  == 14:
                valor = 4004
            if qtd_numeros == 15:
                valor = 6006
            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')

            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_quina, maximo_quina)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_quina, maximo_quina))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))

if op == "4 - lotomania":
        qtd_jogos = st.number_input("Digite a quantidade de jogos da lotomania:", max_value=200, min_value=1)
                
        button = st.button("Confirmar")

        if button:
            qtd_numeros = (50)
            valor = 2.50
            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')
            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_lotomania, maximo_lotomania)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_lotomania, maximo_lotomania))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))

if op == "5 - timemania":
        qtd_jogos = st.number_input("Digite a quantidade de jogos da timemania:", max_value=100, min_value=1)
       
        button = st.button("Confirmar")

        if button:
            valor = 3
            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')

            qtd_numeros = (10)
            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_timemania, maximo_timemania)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_timemania, maximo_timemania))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))
            
            
            time = ['ABC/RN','ALTOS/PI','AMERICA/MG','AMERICA/RN','APARECIDENSE/GO','ATHLETICO/PR','ATLETICO/AC',
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
            def selectRandom(time):
                return random.choice(time)
            st.success("O Time escolhido é:  " + selectRandom(time))
            
if op == "6 - dupla sena":
        qtd_jogos = st.number_input("Digite a quantidade de jogos da dupla sena:", max_value=200, min_value=1)
        qtd_numeros = st.number_input("Digite a quantidade de 6 à 15 números:", max_value=15, min_value=6)
        
        button = st.button("Confirmar")

        if button:

            if qtd_numeros == 6: 
                valor = 2.50 
            if qtd_numeros == 7:
                valor = 17.50
            if qtd_numeros == 8:
                valor = 70
            if qtd_numeros == 9:
                valor = 210
            if qtd_numeros == 10:
                valor = 525
            if qtd_numeros == 11:
                valor = 1155
            if qtd_numeros == 12:
                valor = 2310
            if qtd_numeros == 13:
                valor = 4290
            if qtd_numeros == 14:
                valor = 7507.50
            if qtd_numeros  == 15:
                valor = 12512.50
            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')

            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_duplasena, maximo_duplasena)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_duplasena, maximo_duplasena))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))

if op == "7 - dia de sorte":
        qtd_jogos = st.number_input("Digite a quantidade de jogos do dia de sorte:", max_value=200, min_value=1)
        qtd_numeros = st.number_input("Digite a quantidade de 7 à 15 numeros:", max_value=15, min_value=7)        
        button = st.button("Confirmar")

        if button:

            if qtd_numeros == 7: 
                valor = 2
            if qtd_numeros == 8:
                valor = 16
            if qtd_numeros == 9:
                valor = 72
            if qtd_numeros == 10:
                valor = 240
            if qtd_numeros == 11:
                valor = 660
            if qtd_numeros == 12:
                valor = 1584
            if qtd_numeros == 13:
                valor = 3432
            if qtd_numeros == 14:
                valor = 6864
            if qtd_numeros == 15:
                valor = 12870

            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')

            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_diadesorte, maximo_diadesorte)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_diadesorte, maximo_diadesorte))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))
            meses = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto',
                    'setembro','outubro','novembro','dezembro']
            def selectRandom(meses):
                return random.choice(meses)
            st.success("O mês escolhido é:  " + selectRandom(meses))

if op == "8 - +milionaria":
        qtd_jogos = st.number_input("Digite a quantidade de jogos da + milionária:", max_value=200, min_value=1)
        qtd_numeros = st.number_input("Digite a quantidade de 6 à 12 numeros:", max_value=12, min_value=6)        
        
        button = st.button("Confirmar")

        if button:

            if qtd_numeros == 6: 
                valor = 6 
            if qtd_numeros == 7:
                valor = 42
            if qtd_numeros == 8:
                valor = 168
            if qtd_numeros == 9:
                valor = 504
            if qtd_numeros == 10:
                valor = 1260
            if qtd_numeros == 11:
                valor = 2772
            if qtd_numeros == 12:
                valor = 5544

            total = qtd_jogos
            resultado_vt = valor * total
            texto_resultado_vt = f"R$ {resultado_vt:_.2f}"
            texto_resultado_vt = texto_resultado_vt.replace(".",",").replace("_",".")
            st.success(f'Valor da Aposta {texto_resultado_vt}')

            for indice_jogos in range(qtd_jogos):
                    array_jogos = []
                    for indice_numeros in range(qtd_numeros):
                        numero_sorteado = random.randrange(minimo_milionaria, maximo_milionaria)
                        while numero_sorteado in array_jogos:
                            numero_sorteado = int(random.randrange(minimo_milionaria, maximo_milionaria))
                        array_jogos.append(numero_sorteado)
                        strs = (array_jogos)
                        strs.sort()
                    st.success("JOGO " + str(indice_jogos+1) + ": " + str(strs))
            trevo = [1,2,3,4,5,6]
            trevo_result = []
            def selectRandom(trevo):
                return random.choice(trevo)
            trevo_result = random.sample(trevo,2)
            st.success("O trevo escolhido é: " + str(trevo_result))

            
