import statistics

#Aplicando media
print (statistics.mean([3, 6, 9 ,9]))

#Aplicar mediana 
print (statistics.median([1, 2, 4, 8, 9]))
print (statistics.median([1, 2, 4, 8, 9, 8]))

# Moda 
print (statistics.mode([1, 2, 4, 3, 2]))

# Desvio padroa --- quanto mais proximo de zero indica que os dados estao menos dispercos
print (statistics.stdev([1, 1.5, 2, 4, 4]))