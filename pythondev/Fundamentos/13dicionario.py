# O dicionario pode armazenar valores e propriedades
filmeInception = {
    
    "title" : "Bob Esponja",
    "yearReaase" : 2000,
    "imb" : 8.7,
    "genero" : ["comedia", "drama"]
    
}

# Recuperar elemento do dicionario
print (filmeInception["title"])
print (filmeInception.get("imb"))

# Buscar apenas as chaves
print (filmeInception.keys())

# Buscar apenas os valores
print (filmeInception.values())

# buscar com chave e valor
print (filmeInception.items()) #retorna em forma de tupla

#adicionar nova informacao
filmeInception ["director"] = "Nolan"

# Atualizar itens
filmeInception.update({"imb":8.8})

# remover item
filmeInception.pop("director")

