"""Insira um nome da cidade e veja se ela começa ou não com o nome: Rio"""

def main():
    while True:
        response = input('Diga o nome da cidade: ')
        print('--------------------------------------------------')
        if verificador(response):
            return print('Essa informação é verdadeira. Parabéns, você acertou!')
        else:
            print('Você errou, tente novamente.')
        print('-------------------------------------------------- \n')


def verificador(response):
    return response[:3].lower().strip() == 'rio'

main()