#concatenado valores
name = input ("Digite o nome do filme: \n")
yaerLauch = int (input ( "Digite o ano de lançamento: \n"))
noteMovi = float (input ("Digite a nota do filme: \n"))

print ("Dados do filme: \n")
print ("================")

#primeira forma de concatenar

# print ("Nome do filme: ", name)
# print ("Ano de lançamento: ", yaerLauch)
# print ("Nota do filme: ", noteMovi)

# #alternativa dois

# print ("Nome do filme: ", name, "\nAno de lançamento: ",yaerLauch , "\nNota do filme: ", noteMovi)

#alternativa tres

print (f"Nome do jogo: {name}\n Ano de lançamento {yaerLauch}\n Nota do filme {noteMovi}")