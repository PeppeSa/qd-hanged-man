from .impiccato import *

class ImpiccatoMedio(Impiccato):    
    
    def __init__(self, nickname: str) -> None:
        super().__init__(nickname)   
        self.word: str = super()._getWord('src/db_words/parole_medie.txt')
        self.guessedLetters: str = ["_" for letter in self.word]
    
    