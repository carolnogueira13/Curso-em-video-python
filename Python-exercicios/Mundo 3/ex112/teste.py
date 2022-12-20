# PROGRAMA PARA COLOCAR AS FUNÇÕES DO MODULO EM PACOTES
from utilitarios import moeda, dados

p = dados.leiaDinheiro("Digite o preço: R$ ")
moeda.resumo(p, 35, 22)
