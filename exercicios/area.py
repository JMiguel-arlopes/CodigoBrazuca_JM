def main():
    H = float(input(f'Qual a altura da sua Parede em Metros? '))
    L = float(input(f'Qual a largura da sua Parede em Metros? '))

    A = area(H, L)

    print(f'A Parede que possui dimensões de {H} x {L} tem como Área {A}M')

def area(H, L):
    return H * L

main()