def main():
    co = float(input("Qual medida do Cateto Oposto: "))
    ca = float(input("Qual medida do Cateto Adjacente: "))

    hp = hipotenusa(ca, co)

    print('------------------------------------------------------------')
    print(f'A hipotenusa é exatamente igual a {hp}')
    print('------------------------------------------------------------')


def hipotenusa(ca, co):
    return ((ca**2) + (co**2)) ** (1/2)

main()