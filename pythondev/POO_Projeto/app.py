from modelos.biblioteca import Biblioteca

BibliotecaCidade = Biblioteca("Biblioteca da Cidade")
BibliotecaShopping = Biblioteca("Biblioteca do Shopping")

BibliotecaCidade.alterar_estado()

def main():
    Biblioteca.listar()

if __name__ == "__main__":
    main()