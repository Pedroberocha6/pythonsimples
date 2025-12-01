#Biblioteca dos alimentos
alimentos = {
    
    "Arroz" : 15.5,
    "Feijão" : 8.9,
    "Macarrão" : 6.75
    
}

media = (alimentos.get("Arroz") + alimentos.get("Feijão") + alimentos.get("Macarrão")) / 3

maior = max(alimentos,key = alimentos.get)


print (alimentos)
print (maior)
print (f"{media:.2f}")

