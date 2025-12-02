# fatorial de um numero

def fatorial(num):
    if num == 1:
        return 1
    else:
        return (num * fatorial(num - 1))
    
number = int (input ("Digite um número: \n"))
print (f"O fatorial de {number} é {fatorial(number)}")

# soma total de um numero

def soma(num):
    if num == 1:
        return 1
    else:
        return num + soma (num - 1)

numero = int (input ("Digite um número: \n"))
print (f"A soma dos números até o número {numero} é {soma(numero)}")