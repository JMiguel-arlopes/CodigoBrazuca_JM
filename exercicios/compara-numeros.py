def main():
    num = int(input('Insira o Primeiro número: '))
    num_2 = int(input('Insira o Segundo número: '))
    verificador(num, num_2)


def verificador(num,num_2):
    if num > num_2:
        print(f'O Primeiro Número ({num}) é maior.')
    elif num_2 > num:
        print(f'O Segundo Número ({num_2}) é maior')
    elif num == num_2:
        print(f'O dois números ({num} e {num_2}) são iguais')


main()