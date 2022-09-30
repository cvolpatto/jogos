from cgitb import text
import random
import re
#from tkinter import END, N
import streamlit as st


#st.title('Escolha o jogo desejado') # no meio da tela
arrary_jogos = []
indice_jogos = int(0)
indice_numeros = int(0)
minimo_megasena = int(1)
maximo_megasena = int(61)

op = st.sidebar.selectbox("Escolha o jogo",("SELECIONE","1 - mega-sena","2 - lotofácil","3 - quina","4 - lotomania",
"5 - timemania","6 - dupla sena","7 - dia de sorte"))

if op == "1 - mega-sena":
        qtd_jogos = st.sidebar.number_input("Digite a quantidade de jogos da mega-sena:", max_value=100, min_value=1)
        qtd_numeros = st.sidebar.number_input("Digite a quantidade de 6 à 15 números:", max_value=15, min_value=6)
        
        button = st.sidebar.button("Confirmar")

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
            st.write("jogo" + str(indice_jogos+1) + ": " + str(strs))









