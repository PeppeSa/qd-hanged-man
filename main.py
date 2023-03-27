"""
Created on 14/12/2022



@author Giulia, Giuseppe, Tommaso

"""

from src.classModules.impiccato import Impiccato
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
            hanged: object = Impiccato(nick, lingua, 'easy')
        case 2:
            hanged: object = Impiccato(nick, lingua, 'normal')
        case 3:
            hanged: object = Impiccato(nick, lingua, 'hard')

    hanged.startGame(_)

if __name__ == "__main__":
    main()
