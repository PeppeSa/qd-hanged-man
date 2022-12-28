"""
Created on 14/12/2022

@author Giulia, Giuseppe

"""

import random

from locales.i18n import choose_language, set_locale

def carica_parole():
    livello = input(_('Scegli un livello di gioco:\n1. facile\n2. medio\n3. difficile\n\n'))
    lista_di_parole = []
    
    if livello == '1' :
        with open('src/db_words/parole_facili.txt', 'r') as f:
            for line in f:
                parola = line.rstrip('\n')
                lista_di_parole.append(parola)
     
    elif livello == '2' :
        with open('src/db_words/parole_medie.txt', 'r') as f:
            for line in f:
                parola = line.rstrip('\n')
                lista_di_parole.append(parola)

    elif livello == '3' :
        with open('src/db_words/parole_difficili.txt', 'r') as f:
            for line in f:
                parola = line.rstrip('\n')
                lista_di_parole.append(parola)

    return lista_di_parole
     


def parola_random(lista_di_parole):
    return random.choice(lista_di_parole)

def visualizza_parola(lista_lettere):
    print(' '.join(lettera for lettera in lista_lettere))

def aggiorna_lettere_indovinate(parola, scelta, lettere_indovinate):
    for i, lettera in enumerate(parola):
        if lettera == scelta:
            lettere_indovinate[i] = lettera
    return lettere_indovinate

def show_player_life():

    life = """
---
"""
    yield life

    life = """
|----
|
|
|
|
---
"""
    yield life
    life = """
|----0
|    |
|    |
|    |
|    |
---
"""
    yield life

    life = """
|----O
|    |
|   /|\
|    |
|    |
---
"""

    yield life

    life = """
|----O
|    |
|   /|\
|    |
|   /|\
---
"""

    yield life
    life = """

|--\
|   \O
|    |1
|   /|\
|    |
--- /|\
"""
    yield life


# fai scegliere all'utente la lingua
lingua = choose_language()

# impostala come lingua per questa partita
_ = set_locale(lingua)

lista_di_parole = carica_parole()
parola_da_indovinare = parola_random(lista_di_parole)
lettere_indovinate = ['_' for lettera in parola_da_indovinare]
vita_giocatore = show_player_life()

visualizza_parola(lettere_indovinate)


def choosen_word():
    scelta = input(_('Inserisci una lettera -> '))
    return scelta

while True:
  
    scelta = choosen_word()
    if scelta in parola_da_indovinare:
        lettere_indovinate = aggiorna_lettere_indovinate(parola_da_indovinare, scelta, lettere_indovinate)
        if parola_da_indovinare == ''.join(lettera for lettera in lettere_indovinate):
            print(_('Hai vinto, complimenti! Hai indovinato la parola: %s') % parola_da_indovinare)
            break
    else:
        try:
            print(next(vita_giocatore))
        except StopIteration:
            print(_('Hai perso, la parola era: %s') % parola_da_indovinare)
            break

    visualizza_parola(lettere_indovinate)
