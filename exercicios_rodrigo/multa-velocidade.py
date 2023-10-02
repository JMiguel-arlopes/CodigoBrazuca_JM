def main():
    vel = float(input('Qual sua Velocidade (km/h): '))

    if vel > 80:
        multa = medidor(vel)
        print('Você passou do Limite de 80km/h')
        print(f'Sua multa é de {multa}R$')
    else: 
        print('Está dentro da normalidade, tenha um Bom Dia!')


def medidor(vel):
    acrescimo = (vel - 80)
    price = 7
    if vel > 80:
        return acrescimo * price

main()