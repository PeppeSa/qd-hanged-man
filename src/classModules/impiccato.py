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
    def __init__(self, nickname: str) -> None:
        self.nickname: str = nickname
        self.life: object = self.__show_player_life()
        self.mistakesCounter: int = 0
        self.word: str = "prova" #questo attributo e quello sotto servono solo 
        self.guessedLetters: str = ["_" for letter in self.word] #     per implementare il metodo startGame in mado da farlo ereditare 
    
    def startGame(self) -> None:
        
        while self.mistakesCounter != 6:
            
            letter: str = input(_("\nInserisci una lettera -> "))

            if letter in self.word:
                self.guessedLetters = self.__aggiorna_lettere_indovinate(self.word, letter, self.guessedLetters)
                if self.word == ''.join(letter for letter in self.guessedLetters):
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
    
    
    def __aggiorna_lettere_indovinate(self, parola, scelta, lettere_indovinate): 
        for i, lettera in enumerate(self.word):
            if lettera == scelta:
                lettere_indovinate[i] = lettera
        return lettere_indovinate
    
    def __visualizza_parola(self) -> None:
        print(' '.join(lettera for lettera in self.guessedLetters))

    def __write_in_classifica_txt(self) -> None:
        
        f = open("src/classifica.txt", "a")
        f.write(f"\n{self.nickname} ha vinto con {self.mistakesCounter} errori commessi.")
        f.close()

    
    def __show_player_life(self) -> object:
        
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
        |   /|\\
        |    |
        |    |
        ---
        """

        yield life

        life = """
        |----O
        |    |
        |   /|\\
        |    |
        |   /|\\
        ---
        """

        yield life
        life = """

        |--\\
        |   \O
        |    |
        |   /|\\
        |    |
        --- /|\\
        """
        yield life