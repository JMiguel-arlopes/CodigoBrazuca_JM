""" Sorteia-se um aluno da lista que for inserida ao Main """
from random import randrange

def main():
    candidatos = alunos()
    sorteado = sorteio(candidatos)
    print(f'O aluno sorteado foi {sorteado}')

def alunos():
    alunos = []

    quant = int(input('Quantos alunos você deseja incluir ao sorteio? '))
    for i in range(quant):
        aluno = input(f'Qual o nome do seu {i+1}° Aluno para o sorteio? ').capitalize()
        alunos.append(aluno)

    return alunos

def sorteio(people):
    i = randrange(len(people))
    return people[i]

main()