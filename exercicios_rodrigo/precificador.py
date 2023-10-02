def main():
    distancia = float(input('Qual é a distância da sua viagem? '))

    conta = precificador(distancia)

    print(f'Você está prestes a começar uma viagem de {distancia}Km.')
    print(f'Você pagará uma conta de {conta}R$ pela viagem.')

def precificador(distancia):
    return distancia * 0.45 if distancia >= 200 else distancia * 0.5
    
main()