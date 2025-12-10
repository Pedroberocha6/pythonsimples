import random
# import para gerar números aleatório

# Selecionar valor aleatório de uma lista
lista = [1,7,5,3,8]
print(random.choice(lista))

# 2 gerar números aleatórios em um intervalo
r1 = random.randint(5,20)
print (r1)

# Sorte caractere aleatório
name = "Pedro"
r2 = random.choice(name)
print(r2)

# 4 selecionar mais de um valor 
# random.sample(sequencia, tamnanho)
print (random.sample(lista, 2))
print (random.sample(lista, 5))
s = "olá mundo"
print (random.sample(s, 4))

# Programa de sorteio
done = False
while not done:
    print ("O que deseja fazer? (1) para adivinhar (0) para sair.\n")
    choice = input("> \n")
    if choice == "1":
        print ("Adivinhe um número de 0 a 10 \n")
        num = int (input("Digite um número de 0 a 10: \n"))
        result = random.randint(0, 10)
        if num == result:
            print (f"Você acertou. Era o número {num} \n")
        else:
            print (f"Você errou. Era o número {result} \n")    
    elif choice == 2:
        done = True
    else:
        print ("Escolha a opção correta. \n")