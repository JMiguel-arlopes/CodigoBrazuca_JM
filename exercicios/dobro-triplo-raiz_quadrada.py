def main():
    num = int(input('insira um número: '))

    dob = dobro(num)
    tri = triplo(num)
    raiz = raiz_quadrada(num)

    print('o dobro de {} é {}'.format(num, dob))
    print('o triplo de {} é {}'.format(num, tri))
    print(f'a raíz quadrada de {num} é {raiz}')


def dobro(num):
    return num * 2

def triplo(num):
    return num * 3

def raiz_quadrada(num):
    return num ** (1/2)

main()