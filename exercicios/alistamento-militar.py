from datetime import date
def main():
    age = int(input('Indique sua Data de Nascimento: '))

    atual = date.today().year
    idade = atual - age
    
    alistamento(idade, atual)


def alistamento(idade, atual):
    if idade > 18:
        saldo = idade - 18
        ano = atual - saldo

        print(f'Seu alistamento foi em {ano}')
        print(f'Sua data de alistamento já passou a {saldo} anos.')
    elif idade < 18:
        saldo = 18 - idade
        ano = saldo + atual

        print(f'Falta {saldo} anos para você se alistar')
        print(f'Será no ano de {ano}')
    elif idade == 18:
        print('Você precisa se alistar IMEDIATAMENTE!')

main()
