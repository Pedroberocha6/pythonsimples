# potência de um número
power = lambda num : num **2
print (power(5))

# Verificar de o número é par

par = lambda x : x % 2 == 0

print(par(4))
print(par(7))

#função que divide um num por outro
div_num = lambda x, y: x/y
print (div_num(10, 2))
print (div_num(13, 6))

# função para inverter strings
reverter = lambda s: s[::-1]
print (reverter("Python"))

# funcionalidades relacionadas aos filmes

moviesLists = ["Titanic" , "The God Father", "Inception", "Jurassic Park"]
ratings = {
    
    "Titanic" : [8.5, 9.0, 7.5],
    "The God Father" : [9.5, 9.8, 8.5],
    "Inception" : [8.0, 7.0, 8.5],
    "Jurassic Park" : [7.5, 7.0, 7.5] 
}

# funcoe de calcular a media de rating de um filme
media = lambda movie_name : sum(ratings[movie_name]) / len(ratings[movie_name])



#funcoe verificar se filme esta na lista

check_movie = lambda movie_name: movie_name in moviesLists


# Recomendar pela media de avaliacao
recommendMedia = lambda movieName: f"Recomendo assitir {movieName} com media {media(movieName):.2f}"

###########################################
print (f"Media de avaliacoes do filme e  {media("Titanic")}")
print (f"Incepiction esta na lista? {check_movie("Inception")}")
print (f"{recommendMedia("Jurassic Park")}")