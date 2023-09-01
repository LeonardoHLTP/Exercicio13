#principal.py
from funcoes import cumprimentar

def main():
    nome = input("Digite o seu nome")
    mensagem = cumprimentar(nome)
    print(mensagem)

if __name__ == "__main__":
    main()