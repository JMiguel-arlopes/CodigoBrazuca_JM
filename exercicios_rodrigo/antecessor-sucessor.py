def main():
    num = int(input('Digite um número: '))
    diferenca(num)

def diferenca(num):
    ant = (num - 1)
    suc = (num + 1)
    return print('Baseado em {}, seu antecessor é {} e seu sucessor {}'.format(num, ant, suc))

main()