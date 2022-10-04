from cgitb import text
import random
import re
from selectors import SelectSelector
from tkinter.tix import Select
from django.forms import SelectMultiple
from jinja2 import select_autoescape
#from tkinter import END, N
import streamlit as st
from random import randint
import numpy as np

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
            st.success("O mês escolhido é: " + str(trevo_result))

            
