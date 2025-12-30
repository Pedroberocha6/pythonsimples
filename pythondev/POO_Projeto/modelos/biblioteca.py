class biblioteca:
    
    bibliotecas = []
    
    def __init__(self, nome):
        self.nome = nome
        self.ativo = False
        biblioteca.bibliotecas.append(self) # Adiciona a lista usando o self como palavra reservada
    
    def __str__(self):
        return self.nome #retorna o nome quando usa o print direto
    
    def lista ():
        for biblio in biblioteca.bibliotecas :
            print(f"{biblio.nome} | {biblio.ativo}")
    
bibliotecaCidade = biblioteca("Biblioteca da Cidade") # Instancia o objeto. O nome agora e obrigatorio
bibliotecaCidade = biblioteca("Biblioteca do Shopping")

biblioteca.lista()