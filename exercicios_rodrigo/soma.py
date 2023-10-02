def main():
    x = int(input('Escolha um número para soma: '))
    y = int(input('qual outro número para soma? '))

    result = soma(x, y)
    print(f'a soma de {x} e {y} é', result)

def soma(x, y):
    return x + y

main()