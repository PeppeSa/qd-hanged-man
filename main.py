"""
Created on 14/12/2022

@author Giulia, Giuseppe

"""

import random

from src.i18n import choose_language, set_locale

def choosen_word() -> str:
    scelta = input(_('Inserisci una lettera -> '))
    return scelta

def carica_parole(lingua:str) -> str:
    
    livello = ''
    while(livello not in ['1', '2', '3']):
        livello = input(_('Scegli un livello di gioco:\n1. facile\n2. medio\n3. difficile\n\n'))
    lista_di_parole = []
    
    if livello == '1':
        difficolta = 'easy'     
    elif livello == '2':
        difficolta = 'normal'    
    elif livello == '3':
        difficolta = 'hard'
        
    
    with open('src/db_words/%s/%s.txt' %(lingua, difficolta), 'r') as f:
        for line in f:
            parola = line.rstrip('\n')
            lista_di_parole.append(parola)

    return lista_di_parole
     


def parola_random(lista_di_parole: list[str]) -> str:
    return random.choice(lista_di_parole)

def visualizza_parola(lista_lettere: list[str]) -> None:
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
|  ----



"""
    yield life

    life = """

|----O
|
|
|
|  ----


"""
    yield life

    life = """

|----O
|    |
|    |
|    |
|    |


"""
    yield life

    life = """

|----O
|   /|\
|    |
|    |
|    |
   ----

"""
    yield life

    life = """

|----O
|   /|\
|    |
|    |
    /|\
   -----

"""

    yield life


# fai scegliere all'utente la lingua
lingua = choose_language()

# impostala come lingua per questa partita
_ = set_locale(lingua)

lista_di_parole = carica_parole(lingua)
parola_da_indovinare = parola_random(lista_di_parole)
lettere_indovinate = ['_' for lettera in parola_da_indovinare]
vita_giocatore = show_player_life()

visualizza_parola(lettere_indovinate)


while True:
  
    scelta = choosen_word()
    if scelta in parola_da_indovinare:
        lettere_indovinate = aggiorna_lettere_indovinate(parola_da_indovinare, scelta, lettere_indovinate)
        #if parola_da_indovinare == ''.join(lettera for lettera in lettere_indovinate):
        #riscrivo così:
        if parola_da_indovinare == ''.join(lettere_indovinate):
            print(_('Hai vinto, complimenti! Hai indovinato la parola: ') + parola_da_indovinare)
            break
    else:
        try:
            print(_('La parola non contiene la lettera ') + scelta)
            print(next(vita_giocatore))
            
        except StopIteration:
            print(f'|--\ \n|   \O \n|   /|\ \n|    | \n    /|\ \n  GAME OVER\n')
            print(_('Hai perso, la parola era: ') + parola_da_indovinare)
            break

    visualizza_parola(lettere_indovinate)


