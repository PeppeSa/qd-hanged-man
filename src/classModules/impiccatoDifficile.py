from .impiccato import *


class ImpiccatoDifficile(Impiccato):    
    
    def __init__(self, nickname: str) -> None:
        super().__init__(nickname)   
        self.word: str = super()._getWord('src/db_words/parole_difficili.txt')
        self.guessedLetters: str = ["_" for letter in self.word]
    
    