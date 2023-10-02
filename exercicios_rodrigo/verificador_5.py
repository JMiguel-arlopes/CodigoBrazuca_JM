"""Verifica a Primeira e a Ultima Palavra do seu nome completo """
def main():
    name = input('Digite seu Nome Completo: ').strip().split()

    first_word = fisrt(name)
    last_word = last(name)

    print('----------------------------------------')
    print(f'Seu Primeiro nome é {first_word}')
    print(f'Seu Ultimo nome é {last_word}')
    print('----------------------------------------')

def fisrt(name):
    i = 0
    return name[i]

def last(name):
    i = len(name)-1
    return name[i]

main()