import hashlib

#Verificar algoritmos disponiveis
print (hashlib.algorithms_available)

#verificar algoritmos de acordo com o SO
print (hashlib.algorithms_guaranteed)

# sha_256

algoritmo = hashlib.sha256()
print (algoritmo.digest())
mensagem = "A melhor forma de prever o futuro e cria-lo".encode()
algoritmo.update(mensagem)
print (algoritmo.hexdigest())

# Utilizando MD4
md5 = hashlib.md5()
md5.update(mensagem)
print(md5.hexdigest())