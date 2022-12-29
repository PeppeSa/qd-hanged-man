"""
Created on 14/12/2022

@author Giulia, Giuseppe

"""

import random



def choosen_word() -> str:
    scelta = input('Inserisci una lettera -> ')
    return scelta


def carica_parole() -> list[str]:

    livello = None
    while livello not in ('facile', 'medio', 'difficile'): #controllo sull'input per verificare sia valido
     livello = input('Scegli un livello di gioco:\n1. facile\n2. medio\n3. difficile -> ')

    lista_di_parole = []
    
    if livello == '1' :
      file_name = 'easy.txt'
    elif livello == '2':
      file_name = 'normal.txt'
    elif livello == '3':
      file_name = 'hard.txt'

    with open(file_name, 'r') as f:
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




lista_di_parole = carica_parole()
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
            print(f'Hai vinto, complimenti! Hai indovinato la parola: {parola_da_indovinare}')
            break
    else:
        try:
            print(f'La parola non contiene la lettera {scelta}')
            print(next(vita_giocatore))
            
        except StopIteration:
            print(f'|--\ \n|   \O \n|   /|\ \n|    | \n    /|\ \n  GAME OVER\n')
            print(f'Hai perso, la parola era: {parola_da_indovinare}')
            break

    visualizza_parola(lettere_indovinate)


