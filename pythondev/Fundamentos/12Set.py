filmesSet = {"Bob Esponja","Alvin e os Esquilos","Interrestelar"}

# Buscar quantidade
print (len(filmesSet))

# Valor True e 1 sao iguais
exemploSet = {"Bob",True,1,8.7}
print (exemploSet)

#adiocinao item de outro set
filmesSet.update(exemploSet) # nao adiciona os duplicados

# Remover item do set
filmesSet.remove(True)
filmesSet.remove(8.7)
