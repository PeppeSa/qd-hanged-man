from .impiccato import *


class ImpiccatoDifficile(Impiccato):    
    
    def __init__(self, nickname: str) -> None:
        super().__init__(nickname)   
        self.word: str = self.__getWord()
        self.guessedLetters: str = ["_" for letter in self.word]
    
    def __getWord(self) -> str:
        wordsList: str = []  

        with open('src/db_words/parole_difficili.txt', 'r') as f:
            for line in f:
                word_ = line.rstrip('\n')
                wordsList.append(word_)

        return random.choice(wordsList)  