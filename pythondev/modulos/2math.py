import math

# tomar cuidado com importacao circular deixar nomes diferentes nos modulos

#Acessar o valor de pi
print (f"{math.pi:.2f}")

# numero de euler
print (f"{math.e:.2f}")

#Aredondar numeros para cima e baixo
num = 3.4
print (f"{math.ceil(num)}") # cima 
print (f"{math.floor(num)}") # baixo

# Calcular fatorial
num2 = 6
print (f"{math.factorial(num2)}")

#calcular potencias
print (math.pow(5,5))

# Raiz quadrada de um numero
print (math.sqrt(169))

# MDC
mdc = math.gcd(20,100)
print (mdc)

#logaritimo
print (math.log(10))
