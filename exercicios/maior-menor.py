"""Verifica qual o maior e o menor valor da lista"""

def main():
    size = int(input('Qual o tamanho da sua lista númerica? '))
    result = ordernar(size)
    print(f'Sua lista é {result.split()}')
    result.sort()
    first = result[0]
    last = result[len(result)-1]

    print('-' *35)
    print(f'Dentre sua lista, o MAIOR número é {last}')
    print(f'Enquanto o MENOR número é {first}')
    print('-' *35)

def ordernar(size):
    lista = []
    for i in range(size):
        num = int(input(f'Insira o {i+1}° número da Lista: '))
        lista.append(num)

    return lista

main()