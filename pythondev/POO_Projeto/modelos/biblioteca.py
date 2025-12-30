class biblioteca:
    
    bibliotecas = []
    
    def __init__(self, nome):
        self.nome = nome
        self._ativo = False  #Privado. Ao adicionar o _ eu torno ele em atributo privado e assim apenas a classe tem acesso para alterar o atributo
        
        biblioteca.bibliotecas.append(self) # Adiciona a lista usando o self como palavra reservada
    
    def __str__(self):
        return self.nome #retorna o nome quando usa o print direto
    
    def lista ():
        for biblio in biblioteca.bibliotecas :
            print(f"{biblio.nome} | {biblio.ativo}")
            
    def alterar_estado(self):
        self._ativo = not self._ativo
        
    @property
    def ativo(self):
        return "Ativada." if self._ativo else "Desativada." # Metodo set
    
bibliotecaCidade = biblioteca("Biblioteca da Cidade") # Instancia o objeto. O nome agora e obrigatorio
bibliotecaCidade.alterar_estado()
bibliotecaCidade = biblioteca("Biblioteca do Shopping")

biblioteca.lista()