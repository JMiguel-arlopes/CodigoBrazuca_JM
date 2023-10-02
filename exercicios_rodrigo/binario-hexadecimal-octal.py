def main():
    num = int(input('Insira um número inteiro qualquer: '))
    choice = int(input("""Escolha uma opção de 1 a 3 para conversão:
    [1] BINARIO
    [2] OCTAL
    [3] HEXADECIMAL
    Sua opção: """))
    result_binario = binario(num)
    result_octal = octal(num)
    result_hexa = hexa(num)

    match choice:
        case 1:
            print(f'O seu resultado em BINÁRIO é: {result_binario[2:]}')
        case 2:
            print(f'O seu resultado em OCTAL é: {result_octal[2:]}')
        case 3:
            print(f'O seu resultado em HEXADECIMAL é: {result_hexa[2:]}')


def binario(num):
    return bin(num)

def octal(num):
    return oct(num)

def hexa(num):
    return hex(num)

main()