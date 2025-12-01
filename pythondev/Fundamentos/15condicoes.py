# informações do filme
# name = input ("Digite o nome o filme: \n")
# yearRelease = int (input ("Ano de lançamento: \n"))
# rating = float (input ("Digite a nota: \n"))

# #condições 
# if  yearRelease > 2015 and rating > 8:
#     print (f"O filme {name} é muito bom. Recomendo.\n")
# else:
#     print (f"Não recomendo o filme {name}\n")

num1 = float (input("Digite um número: \n"))
num2 = float (input ("Digite o segundo número: \n"))
opercao = input ("Digite a opreção a ser feita (- + * /): \n")

if  opercao == "+":
    result = num1 + num2
    
elif    opercao == "-":
    result = num1 - num2

elif opercao == "*":
    result = num1 * num2
    
elif opercao == "/":
    if  num2 != 0:
        result = num1 / num2
    else:
        print ("Erro divisão por 0")
        result = 0
else:
    print ("Opreção inválida.")

print (f"Resultado é {result:.2f}")
