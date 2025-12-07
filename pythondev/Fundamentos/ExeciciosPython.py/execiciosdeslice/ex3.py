frutas = ['maçã', 'banana', 'laranja', 'morango', 'uva']

#Crie uma cópia rasa (shallow copy) da lista frutas numa nova variável chamada frutas_copia usando a notação de slice completa.
novaLista = frutas[:]
print (novaLista)

#Usando slice por atribuição, substitua 'laranja' e 'morango' por 'kiwi' e 'abacaxi' na lista frutas original.
frutas [2:4] = ["kiwi" , "abacaxi"]
print (frutas)

#Usando slice por atribuição, insira 'pera' e 'limão' entre 'banana' e 'kiwi' (use a lista modificada do exercício 12).
frutas [2:2] = ["pera" , "limao"]
print (frutas)

#Usando slice por atribuição, remova os 3 últimos elementos (kiwi, abacaxi, uva) da lista
frutas [4:7] = []
print (frutas)