"""
*args ultilizamos quando não sabemos a quantidade de argumentos que teremos em uma função
- argumentos são passados em tuplas, ou seja, uma lista imutável na execução do código


**Kwargs além de valores passa também as chaves de cada argumento
E os argumentos são passados como dicionários 
"""

# Soma de números

def soma(*num):
    sumTotal = 0
    for n in num:
        sumTotal += n
    print (f"Soma é {sumTotal}")
    
soma (7)
soma (7,9)

# usando kwargs

def apresentacao(**data):
    for key, velue in data.items():
        print (f"{key} - {velue}")
        
apresentacao (name = "Python", category = "Backand", level = "Iniciante")
apresentacao (name = "Desenvolvimento de IA", category = "IA", level = "Intermediário")
