# Classe Geral (Super Clase) guarda os metodos importantes para outras classes
class Game:
    
    total_Games = 0 # Variavel para contar a quantidade de jogos
    
    def __init__(self, name = "" , yearLaucher = 0, note = 0, multiplayer = 0):
        self.name = name
        self.yearLaucher = yearLaucher
        self.note = note 
        self.multplayer = multiplayer
        Game.total_Games +=  1 # Toda vez que iniciar a instancia ele soma mais 1
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
        
# Classe derivada ou Especializada. Herda os metodos da classe Geral
class SinglePlayer(Game):
    def __init__(self, name = "" , yearLaucher = 0, note = 0, storyLine = ""):
        super().__init__(name, yearLaucher, multiplayer = False , note = 0)
        self.storyLine = storyLine
        
    def ficha(self):
        super().ficha()
        print (f"Enredo: {self.storyLine}") 
     
        
    
game1 = Game("Agar.io", 2015, 4, True)
game1.ficha()

gameOf = SinglePlayer ("Zelda" , 2020, 9, "Exploracao de mundo aberto")
gameOf.ficha()




 