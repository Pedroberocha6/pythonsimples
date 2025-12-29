class Game:
    
    def __init__(self, name = "" , yearLaucher = 0, note = 0, multiplayer = 0):
        self.name = name
        self.yearLaucher = yearLaucher
        self.note = note 
        self.multplayer = multiplayer
        self.total = 0
        self.avaliacoes = 0
    
    def __str__(self):
        return f"Game: {self.yearLaucher}"
    
    def ficha(self):
        print ("--- Dados do Jogo ---")
        print (f"Nome do jogo: {self.name}")
        print (f"Ano do lancamento: {self.yearLaucher}")
        print (f"Nota do jogo: {self.note}")
        print (f"Possui multplayer? {self.multplayer}")
        
    def avaliacao (self, note):
        self.total += note
        self.avaliacoes += 1
        
    def media(self):
        print (f"Media do jogo {self.name}: {self.total / self.avaliacoes} ")
        
    
game1 = Game("Zelda", 2017, 9, False)
game2 = Game("God Of War", 2018, 8, False)

game1.ficha()
game2.ficha()

game1.avaliacao(9)
game1.avaliacao(6)
game1.media()


 