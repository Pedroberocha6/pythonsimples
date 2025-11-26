num1 = int (input ("Digite um numero: \n"))
num2 = int (input ("Digite outro: \n"))

#aritimecos 

sum = num1 + num2
sub = num1 - num2
div = num1 / num2 
mult = num1 * num2

bigger = num1 > num2 
smaller = num1 < num2
equal = num1 == num2 
different = num1 != num2 
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2


print (f"Os numeros {num1} e {num2} são iguais? {equal} \n ")
print (f"O número {num1} é maior ou igual ao {num2}? {bigger_equal} \n ")

#atribuidores

num1 += 1
num1 -= 1
num1 *= 1
num1 /= 1