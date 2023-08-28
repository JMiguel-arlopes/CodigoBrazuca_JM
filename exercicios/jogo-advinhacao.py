from random import randint

def main():
    print('Vamos jogar um pouco?')
    print('Pensei num número de 1 a 5, tente advinhar qual é!')

    while True:
        try:
            chute = int(input('Advinhe o número que estou pensando: '))
            verifica(chute)
        except ValueError as erro:
            print('\n ATENÇÃO: Cuidado..')
            print(f"Você cometeu um erro: {erro}")
        
        result = number(1, 5)

        if result == chute:
            return print(f'Parabéns, Você acertou! Era o número {result}')
        else:
            print("Errou o número, tente novamente..")
    

def number(x, y):
    return randint(x, y)

def verifica(num):
    if num > 5 or num < 1:
        raise  ValueError('O número está fora de alcance.')
    return num

main()