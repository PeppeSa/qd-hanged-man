import random
"""
Classe base che racchiude il funzionamento del gioco , con l'aggiunta di un metodo per scrivere, in caso di vittoria,
il nickname dell'utente in un file di testo classifica.txt

- alla riga  per mostrare  le varie fasi dell'impiccato dato che 
  nel codice precedente era un oggetto di tipo generator 
  ho creato  l'attributo life di tipo object che prende in input 
  quello che ritorna il metodo __show_player_life() che è la stessa
  funzione che c'era prima   
  
"""
class Impiccato:
    def __init__(self, nickname: str, language: str, difficulty: str) -> None:
        self.nickname: str = nickname
        self.life: object = self.__show_player_life()
        self.mistakesCounter: int = 0
        self.guessedLetters: str = "_"
        self.language: str = language
        self.difficulty: str = difficulty
        
    
    def startGame(self, _) -> None:
        self.word = self._getWord()
        self.guessedLetters = ["_" for letter in self.word]
        while self.mistakesCounter < 6:
            
            letter: str = input(_("\nInserisci una lettera -> "))

            if letter in self.word:
                self.guessedLetters = self.__aggiorna_lettere_indovinate(self.word, letter, self.guessedLetters)
                if self.word == ''.join(self.guessedLetters):
                    self.__write_in_classifica_txt()                    
                    print(_(f"{self.nickname} hai vinto, complimenti! Hai indovinato la parola: {self.word}"))
                    break
            else:
                self.mistakesCounter += 1
                print(next(self.life))
            print("\n")        
            self.__visualizza_parola()
        if self.mistakesCounter == 6:
            print(_(f"{self.nickname} hai perso, la parola era: {self.word}"))
    
    
    def __aggiorna_lettere_indovinate(self, parola: str, scelta: str, lettere_indovinate: str): 
        for i, lettera in enumerate(self.word):
            if lettera == scelta:
                lettere_indovinate[i] = lettera
        return lettere_indovinate
    
    def __visualizza_parola(self) -> None:
        print(' '.join(self.guessedLetters))

    def __write_in_classifica_txt(self, _) -> None:
        
        with open("src/classifica.txt", "a") as f:
            f.write(_("\n{self.nickname} ha vinto con {self.mistakesCounter} errori commessi."))

    def _getWord(self) -> str:
        file_path = 'src/db_words/'+self.language+'/'+self.difficulty+'.txt'
        wordsList: str = []

        with open(file_path, 'r') as f:
            for line in f:
                word_: str = line.rstrip('\n')
                wordsList.append(word_)

        return random.choice(wordsList) 
    

    def __show_player_life(self) -> object:
        
        yield """
        ---
        """
        

        yield """
        |----
        |
        |
        |
        |
        ---
        """
        
        yield """
        |----0
        |    |
        |    |
        |    |
        |    |
        ---
        """
        

        yield """
        |----O
        |    |
        |   /|\\
        |    |
        |    |
        ---
        """

        

        yield """
        |----O
        |    |
        |   /|\\
        |    |
        |   /|\\
        ---
        """

        
        yield """

        |--\\
        |   \O
        |    |
        |   /|\\
        |    |
        --- /|\\
        """
        