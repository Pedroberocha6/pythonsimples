class Game:
    
    def __init__(self, name = "" , yearLaucher = 0, note = 0, multiplayer = 0):
        self.name = name
        self.yearLaucher = yearLaucher
        self.note = note 
        self.multplayer = multiplayer
    
    def __str__(self):
        return f"Game: {self.yearLaucher}" #Imprime o que quero mostrar ao chamar o objeto de forma direta
        
    
game1 = Game("Zelda", 2017, 9, True)
game2 = Game("God Of War", 2018, 8, False)

print ("--- Dados do Jogo ---")
print (f"Nome do jogo: {game1.name} \nAno de lacamento: {game1.yearLaucher}\n ")
print (f"Nome do jogo: {game2.name} \nAno de lacamento: {game2.yearLaucher}\n ")