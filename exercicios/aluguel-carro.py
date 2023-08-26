def main():
    timing = int(input('Quantas horas você alugou o Carro? '))
    km = int(input('Quantos KM você rodou no carro? '))

    conta = aluguel(km, timing)

    print('--------------------------------------------------------------------------')
    print(f'Devido os seus {km}Km rodados e {timing} horas, sua conta deu {conta}R$')
    print('--------------------------------------------------------------------------')

def aluguel(km, t):
    distancia = km * 0.45
    timing = t * 60
    
    return distancia + timing

main()