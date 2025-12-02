def welcome():
    print ("Seja bem vindo!")
    
# for i in range(10):
#     welcome()

#funcao de calcular media 

def calcularMedia():
    
    notas = int (input ("Digite quantas notas quer digitar: \n"))
    total = 0
    for i in range(notas):
        nota = float (input("Digite a nota: \n"))
        total += nota
    if notas > 0:
        media = total / notas
    else:
        print("Media igual a 0")
        
    return media

media = calcularMedia()
print (f"A média das avaliações é {media:.2f} \n")

#função para cadastrar um nome

def cadastro():
    name = input ("Digite o nome do filme: \n")
    yaerLauch = int (input ( "Digite o ano de lançamento: \n"))
    moviePrice = float (input("Digite o preço do filme: \n"))
    noteMovi = float (input ("Digite a nota do filme: \n"))
    print (f"{name} - ({yaerLauch}) - R${moviePrice} \n")
    
cadastro ()
cadastro ()