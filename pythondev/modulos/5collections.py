from collections import Counter, namedtuple, deque
from operator import itemgetter 

# Lista de contagem
frutas = ["uva" ,"maca","banana", "abacaxi", "uva", "abacaxi", "laranja", "uva"]
print (Counter(frutas))

# Utilizando tupla nomeada
game = namedtuple("game",["name", "price", "note"])
g1 = game ("Ffia 25", 4, 4.0)
g2 = game ("Resident Evil", 300, 9)
print (g1)
print (g2)

# Ordenar dicionarios 
students = {"Pedro":23 , "Lucas": 20 , "Augusto" : 50, "Romulo": 9}
a = sorted(students.items(), key = itemgetter(1)) # Ordem númerica
a1 = sorted(students.items(), key = itemgetter(0)) # Ordem alfabetica
print (a) 
print (a1)

# Utilizando filas em ambas extremidades
deq = deque([20,40,60,80])
deq.appendleft(10) #adiciona a esquerda
print(deq)
deq.append(90)
deq.popleft()#exclui a esquerda
deq.pop() #exclui a direita
print(deq)