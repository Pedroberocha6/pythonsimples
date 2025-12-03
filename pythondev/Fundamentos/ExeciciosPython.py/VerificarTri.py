def receberLados():
    ladoA = float (input ("Digite um dos lados do triângulo: \n"))
    while ladoA < 0:
        ladoA = float (input ("Valor inválido. Digite novamente: \n"))
    ladoB = float (input ("Digite o outro lado do triângulo: \n"))
    while ladoB < 0:
        ladoB = float (input ("Valor inválido. Digite novamente: \n"))
    ladoC = float (input ("Digite o ultimo lado do triângulo: \n"))
    while ladoC < 0:
        ladoC = float (input ("Valor inválido. Digite novamente: \n"))
    return ladoA, ladoB, ladoC
    
    
def DefinirTri(ladoA, ladoB, ladoC):
    if  ladoA + ladoB > ladoC and ladoA + ladoC > ladoB and ladoC + ladoB > ladoA:
        if ladoA == ladoB and ladoB ==  ladoC:
            print ("Possível forma um triângulo equílatero. \n")
        elif ladoA == ladoB or ladoB == ladoC or ladoC == ladoA:
            print ("Possível formar um triângulo isóceles")
        else:
            print ("Possível formar um triângulo escaleno")
        
    else:
        print ("Não é possível formar uma triângulo. \n")
    



l1, l2, l3 = receberLados()
DefinirTri (l1, l2, l3) 