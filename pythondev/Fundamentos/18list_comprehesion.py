# listar valores de 0 a 10 que são menores de 4
listNumber = [i for i in range(10)if i < 4]
print (listNumber)

# Nomes que possuem letra i 
nomes = ["Bob" , "Alvin", "Cris", "Adam" ]
nomeCom_e = [nome for nome in nomes if 'i' in nome.lower()] 
print (nomeCom_e)

# Nomes já não ultilizados
nomesUtilzados = [nome for nome in nomes if nome != "Cris"]
print (nomesUtilzados)

# Encontrando um filme pelo nome 
while True:
    nomeProcurado = input ("Digite qual nome deseja buscar ou sair para encerrar: \n").lower()
    if nomeProcurado.lower() == "sair":
        print("Programa encerrado.\n")
        break
    
    foundNome = [nome for nome in nomes if nomeProcurado.lower() in nome.lower()]
    if foundNome:
        print (f"Filmes concontrados com o {nomeProcurado}: \n")
        for foundNome in foundNome:
            print(foundNome)
    else:
        print(f"Sem nome encontrado com o nome {nomeProcurado}. Tente novamente: \n")
        
        