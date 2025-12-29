class Game:
    name = ""
    yearLaucher = 0
    multplayer = False
    note = 0
    
# Primeiro jogo
game1 = Game()
game1.name = "Zelda"
game1.yearLaucher = 2017
game1.multplayer = False
game1.note = 9.5

# Segundo jogo
game2 = Game()
game2.name = "Fotinite"
game2.yearLaucher = 2017
game2.multplayer = True
game2.note = 6

# Terceiro Game
game3 = Game()
game3.name = "God Of War"
game3.yearLaucher = 2018
game3.multplayer = False
game3.note = 9

# Quarto Game
game4 = Game ()
game4.name = "Super Mario"
game4.yearLaucher = 1998
game4.multplayer = False
game4.note = 9.8

print ("--- Dados do Jogo ---")
print (f"Nome do jogo: {game1.name} \nAno de lacamento: {game1.yearLaucher}\n ")
print (f"Nome do jogo: {game2.name} \nAno de lacamento: {game2.yearLaucher}\n ")