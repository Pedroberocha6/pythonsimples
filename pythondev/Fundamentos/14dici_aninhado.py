import pprint

filmes = {
    
    "Bob" : {
    "title" : "Bob Esponja",
    "yearReaase" : 2000,
    "imb" : 8.7,
    "genero" : ["comedia", "drama"]
    },
    "interrestelar":{
        
    "title" : "interrestelar",
    "yearReaase" : 2014,
    "imb" : 9.0,
    "genero" : ["Fic", "Drama"]
    },
    "Todo mundo em panico":{
        
    "title" : "interresTodo mundo em panicotelar",
    "yearReaase" : 2006,
    "imb" : 5.0,
    "genero" : ["Comedia", "+18"]
        
    }
    
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmes)

#Buscar informacao no dicionario aninhado
print (filmes["Bob"]["genero"])

#adicionar novo item
filmes ["Bob"["diretor"]] = "Cris"

#excluir dicionario
del filmes ["Bob"]