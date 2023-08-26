def main():
    preco = int(input('Quanto deu sua conta na loja? '))
    valor = desconto(preco)
    print(f'Você ganhou um desconto de 15%, diminuindo sua conta para {valor}R$')

def desconto(x):
    return x * (85/100)

main()