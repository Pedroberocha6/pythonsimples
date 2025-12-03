def verificar (a):
    while a < 0:
        a = float (input ("Valor inválido. Digite novamente: \n"))

def receberLados():
    ladoA = float (input ("Digite um dos lados do triângulo: \n"))
    verificar(ladoA)
    ladoB = float (input ("Digite o outro lado do triângulo: \n"))
    verificar(ladoB)
    ladoC = float (input ("Digite o ultimo lado do triângulo: \n"))
    verificar (ladoC)
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
    

while True:
    op = int (input("Deseja verificar se os lados formam um triângulo? (1) para sim e (0) para sair. \n"))
    while op != 1 and op != 0:
        op = int (input ("Opção inválida. Digite novamente (1) para sim e (0) para sair. \n"))
    if op == 0:
        print ("Programa finalizado.")
        break
    else:
        l1, l2, l3 = receberLados()
        DefinirTri (l1, l2, l3) 
        
