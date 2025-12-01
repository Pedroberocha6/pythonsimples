# Lista de nomes
nomes = ["Bob" , "Alvin", "Cris", "Adam" ]

# iterar valores de uma lista

# for nome in nomes:
#     print (nome)

# ultilizando break
# for nome in nomes:
#     print (nome)
#     if  nome == "Cris":
#         break

# Quando a condição é atendida, vai para a próxima iteração
# for nome in nomes:
#     if nome == "Cris":
#         continue
#     print (nome)

# Avalição do filme
name = input ("Digite o nome o filme: \n")
rating = int (input ("Digite a quantas avaliações deseja fazer: \n"))
total = 0 

for i in range(rating):
    note = float (input ("Digite a nota para o filme: \n"))
    total += note

if total > 0:
    media = total / rating
else:
    media = 0

print (f"A média do filme {name} é {media}")