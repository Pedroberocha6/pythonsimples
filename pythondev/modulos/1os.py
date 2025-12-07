import os

# retornar pasta atual
print (os.getcwd())

#listar arquivos e pastas
print (os.listdir())

# verificar versao do SO
os.system('ver') #simula um comando no terminal

# configuracoes da maquina
os.system('systeminfo')

# limpar tela do terminal
os.system('cls')

# desligar o pc
os.system('shutdown /s')

os.system('shutdown /s /t /0')

# desligar o pc em 1 hora
os.system('shutdown /s /t /3600')

#cancela desligamento
os.system('shutdown /a')

