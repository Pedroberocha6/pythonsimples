# nomes = ["Bob" , "Alvin", "Cris", "Adam" ]

# # Iterando ima lista com while
# index = 0
# # while index < len(nomes):
# #     print (nomes[index])
# #     index += 1

# # Para quando atender a condição

# while index < len(nomes):
#     if nomes [index] == "Cris":
#         break
#     print (nomes[index])
#     index += 1

# #Quando for atendido vai para a próxima iteração
# while index < len(nomes):
#     if nomes [index] == "Cris":
#         index += 1
#         continue
#     print (nomes[index])
#     index += 1
    
    
# Avaliação do filme
  
name = input ("Digite o nome o filme: \n")
rating = int (input ("Digite a quantas avaliações deseja fazer: \n"))
total = 0 
cont = 0

while cont < rating:
    total += float (input("Digite a nota: \n"))
    cont += 1
    
print (f"A nota do filme {name} é {total}")