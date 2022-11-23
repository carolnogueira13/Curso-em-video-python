# PROGRAMA SISTEMA INTERATIVO DE AJUDA EM PYTHON
from time import sleep

c = ("\033[m",
     "\033[30;41m",  # vermelho
     "\033[30;42m",
     "\033[30;43m",
     "\033[30;44m",  # azul
     "\033[30;45m",  # rosa
     "\033[30;47m",  # cinza
     )


def ajuda(comando):
    título(f"Acessando o manual do comando '{comando}'", 6)
    print(c[1], end='')
    help(comando)
    print(c[0], end='')
    sleep(1)


def título(mensagem, cor=0):
    tam = len(mensagem) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f" {mensagem}")
    print("~" * tam)
    print(c[0], end="")
    sleep(0.5)


while True:
    título("Sistema de ajuda Pyhelp", 5)
    msg = input("\033[mFunção ou biblioteca > ")
    if msg.upper() == "FIM":
        título("Até logo", 1)
        break
    else:
        ajuda(msg)
