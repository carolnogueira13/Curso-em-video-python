from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = "cursoemvideo.txt"
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(["Ver pessoas cadastradas", "Cadastrar uma nova pessoa", "Sair do Sistema"])
    if resposta == 1:
        # Opção de listar o conteúdo do arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        # Opção para escrever no arquivo
        cabeçalho('Novo cadastro')
        nome = str(input("Nome: "))
        idade = leiaInt("Idade: ")
        escreverArquivo(arq, nome, idade)
    elif resposta == 3:
        cabeçalho("Saindo do sistema")
        break
    else:
        print("ERRO! Digite uma opção válida!")
    sleep(1)
