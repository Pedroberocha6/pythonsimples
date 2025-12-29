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
        
class gameStudio:
    def __init__(self, name = ""):
        self.name = name
        self.games = []
        
    def add_game(self, game): 
        self.games.append(game)
        
    def evalueteStudio(self):
        total_games = sum ( game.note for game in self.games)
        numGames = len (self.games)
        if numGames == 0:
            print (f"Nenhum jogo lancado pelo estudio {self.name} .")
        else:
            media = total_games / numGames
            print (f"Avaliacao do estudio {self.name}: {media:.2f}")

game1 = Game("Zelda", 2017, 9, False)
game2 = Game("God Of War", 2018, 8, False)
game3 = Game ("Agar.io" , 2011, 8, True)

studio = gameStudio("Awesome Games")
studio.add_game (game1)
studio.add_game (game2)
studio.add_game (game3)

studio.evalueteStudio()
for game in studio.games:
    game.ficha()