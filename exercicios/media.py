def main():
    nota_1 = float(input('Qual sua primeira nota? '))
    nota_2 = float(input('Qual sua segunda nota? '))

    mediaPronta = media(nota_1, nota_2)
    print('Sua média é', mediaPronta)

def media(x, y):
    return (x + y)/2

main()