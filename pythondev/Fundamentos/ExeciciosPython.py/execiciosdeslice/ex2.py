alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
palavra = "Programacao"

#Do alfabeto, crie um slice que pegue um elemento sim, um não, começando pelo 'a'
print (alfabeto[::2])

#Do alfabeto, crie um slice que pegue os elementos do 'c' até o 'h', mas apenas os ímpares (considerando a sub-sequência).
print (alfabeto[2:-3:2])

#Da palavra, crie um slice que pegue apenas as letras nas posições pares (índice 0, 2, 4...).
print (palavra[::2])

#Truque comum! Inverta completamente a lista alfabeto usando a notação de slice com passo negativo.
print (alfabeto[::-1])

#Truque comum! Inverta completamente a palavra usando a notação de slice com passo negativo.
print (palavra[::-1])