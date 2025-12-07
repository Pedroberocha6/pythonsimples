import re

text = "Udemy tem muitos cursos"

#Indicie inicial e final de palavras
# O r significa uma raw (string bruta)
match = re.search(r'muitos cursos', text)
print (f"Inicial: {match.start()}")
print (f"Inicial: {match.end()}")

# Buscar indice do ponto
site = "http://udemy.com"
match = re.search(r'\.', site)
print (f"Onde se encontra o ponto: {match}")

#Buscar lista de caracteres em frase
padrao = "[a-m]" # Caracteres da letra a ate a letra m
result = re.findall(padrao, text)
print (result)

# Verificar inicio ed uma string
rule = r'^A'
listas = ["A casa esta suja", "O dia esta lindo", "Vamos da um passeio" ]
for f in listas:
    if re.match(rule, f):
        print (f"Corresponde {f}")
    else:
        print (f"Nao corresponde {f}")
        
ruleEnd = r'!$'
phrase2 = "O dia esta lindo!"
corresponde = re.search(ruleEnd, phrase2)
if  corresponde:
    print ("Sim, corresponde")
else:
    print ("Nao corresponde.")