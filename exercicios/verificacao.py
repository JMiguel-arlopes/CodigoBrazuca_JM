def main():
    """Resposta: Rio de Janeiro"""
    verificador()


def verificador():
    while True:
        name = input('Qual o nome da cidade de JM: ')
        adaptado = name.lower().strip()

        if adaptado == 'rio de janeiro':
            return print('Parabéns, Você acertou.')
        else:
            print('Você errou feio. Tente Novamente \n')
    
main()