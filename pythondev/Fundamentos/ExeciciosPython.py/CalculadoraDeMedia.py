def receberNote ():
    nota = float (input("Digite sua nota: \n"))
    while nota < 0 or nota > 10:
        nota = float (input ("Nota inválida. Digite novamente: \n"))
    return nota


def calcMedia(x, y):
    
    total = sum(x) 
    return total / y

def mostrarNotas (x):
    if x >= 7:
        print (f"Aluno aprovado com uma média: {x:.2f} ")
    else:
        print (f"Aluno reprovado com uma média: {x:.2f} ")



while True:
    
    op = int (input("Deseja calcular sua média? (1) para sim e (0) para sair. \n"))
    while op != 1 and op != 0:
        op = int (input ("Opção inválida. Digite novamente (1) para sim e (0) para sair. \n"))
    if op == 0:
        print ("Programa finalizado.")
        break
    else:
        listaNotas = []
        quntd_notas = int (input("Quantas notas deseja calcular? \n"))


    for i in range(quntd_notas):
        obtida = receberNote()
        listaNotas.append(obtida)
    
    media = calcMedia(listaNotas, quntd_notas)
    mostrarNotas (media)