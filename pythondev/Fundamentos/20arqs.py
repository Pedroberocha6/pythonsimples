# Função para imprimir nome

def fullName (fistName, lastName):
    print (f"Nome é {fistName} {lastName}")
    
fullName ("Pedro", "Bernardo")
fullName ("João", "Miguel")

def sum_numbers(a,b):
    return a + b

print (f"A soma é {sum_numbers(10,40)}")

#função com parâmentros default

def adress(coutry = "Brasil"):
    print (f"{coutry}")
    
adress()
adress("Espanha")

# avaliar filme

def avaliacao(MovieName, numRatings):
    total = 0
    for i in range(numRatings):
        note = float (input("Digite a nota para o filme: \n"))
        total += note
        
    if numRatings > 0:
        media = total / numRatings
    else:
        media = 0
    print (f"Media do filme {MovieName} é {media}")
    
avaliacao ("Bob", 2)