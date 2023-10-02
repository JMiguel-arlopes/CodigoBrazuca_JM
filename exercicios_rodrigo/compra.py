def main():
    conta = float(input('Quanto deu sua COnta: '))
    pagamento = int(input("""Como deseja realizar sua compra?
    [1] A vista no Dinheiro
    [2] A vista no cartão
    [3] Parcelado 5x
    [4] Parcelado 10x"""))


match pagamento:
    case 1:
        print(f'{conta - (10/100 * conta)}')
    case 2:
        print(f'{conta - (5/100 * conta)}')
    case 3:
        print(f'{conta + (5/100 * conta)}')
    case 4:
        print(f'{conta + (10/100 * conta)}')
 