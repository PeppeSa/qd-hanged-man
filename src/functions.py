
def setDifficulty(_) -> int:

    flag = False
    lvl: int = 0

    while True:
        
        lvl = int(input(_('\nScegli un livello di gioco:\n1. facile\n2. medio\n3. difficile\n\n')))

        if lvl == 1 or lvl == 2 or lvl == 3:
            
            return lvl       
     
        
    

def getNickname(_) -> str:
    
    nick: str = input(_("\nInserisci un nickname (in caso di vittoria sara' salvato in un file di testo insieme al num di errori che hai commesso)\n\n")) 

    return nick