movieDescription = """Top gun, e um filme muito, consagrado na, industria"""
movieName = "Top gun"

#deixar tudo em maiusculo
print (movieName.upper())

# tudo minusculo 
print (movieName.lower())

# deixar a primeira letra em maiusculo
print (movieName.capitalize())

# Deixa a primeira de cada palavra
print (movieName.title())

#retorna centralizada com preenchimento
print (movieName.center(10, '-')) 

# Retornar posição de um caractere
print (movieName.find("u"))

#contar qnts letras existem
print (movieName.find("o"))

# trocar posições
print (movieName.replace("Top","Matrix"))
print (movieName.replace(" "," ")) #remove os espacos

# quebra a string
print (movieDescription.split(','))

