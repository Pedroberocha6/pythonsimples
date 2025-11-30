FilmesList = ["Bob Esponja","Alvin e os Esquilos","Interrestelar", "La vem os pais","Hora do rush"]

#tamanho da lista
print (len(FilmesList))

# recuperar item pelo nome
print (FilmesList.index("Bob esponja"))

#adicionar ao final da lsita
FilmesList.append ("Senhor dos aneis")

# 4 Ordenar a lista 
FilmesList.sort()

# copiar de uma lista para outra
FilmesCopy = FilmesList.copy()
FilmesCopy.remove("Bob Esponja")

# remover todos os itens
FilmesList.clear()