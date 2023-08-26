"""Sabendo que alunos irão realizar uma apresentação, o professor estava com dificuldades em 
descobrir qual seria a ordem dela"""

from random import shuffle

def main():
    quant = int(input('Quantas pessoas participarão da Apresentação? '))
    result = listagem(quant)

    print(f'a ordem das apresentações será {result}')


def listagem(quant):
    lista = []
    
    for i in range(quant):
        pessoa = input(f'Qual o nome do {i+1}° da lista?')
        lista.append(pessoa)
    
    return embaralha(lista)

def embaralha(lista):
    shuffle(lista)
    return lista

main()

