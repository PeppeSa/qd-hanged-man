"""
Created on 14/12/2022



@author Giulia, Giuseppe, Tommaso

"""

import random

from src.i18n import choose_language, set_locale

def choosen_word() -> str:
    scelta = input('Inserisci una lettera -> ')
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



from src.classModules import ImpiccatoFacile, ImpiccatoMedio, ImpiccatoDifficile
from src.functions import setDifficulty, getNickname
from src.i18n import choose_language, set_locale



def main() -> None:
    # fai scegliere all'utente la lingua
    lingua = choose_language()

    # impostala come lingua per questa partita
    _ = set_locale(lingua)

    livDifficolta: int = setDifficulty()
    nick: str = getNickname()

    #il controllo sulla correttezza del livDifficoltà viene fatto in setDifficulty()
    #lo "switch" serve solo per creare l'oggetto associato al liv di difficoltà
    match livDifficolta:
        case 1:
            hanged: object = ImpiccatoFacile(nick)
        case 2:
            hanged: object = ImpiccatoMedio(nick)
        case 3:
            hanged: object = ImpiccatoDifficile(nick)

    hanged.startGame()

if __name__ == "__main__":
    main()
