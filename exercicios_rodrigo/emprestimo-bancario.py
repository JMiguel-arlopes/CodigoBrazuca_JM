"""Perguntando salário preço e quantos anos irá pagar uma casa, precisamos
verificar se o banco pode dar o empréstimo sabendo que
o valor da prestação não pode passar dos 30% de seu salário."""
def main():
    salario = float(input('Digite seu salário: '))
    preco = float(input('Qual o preco da sua casa?'))
    anos = int(input('Quantos anos você quer pagar a casa?'))

    print('-'*35)
    if aprovacao(salario, preco, anos):
        print('Seu Empréstimo foi CONCEDIDO.')
    else:
        print('Empréstimo NEGADO.')
    print('-'*35)

def aprovacao(s, p, a):
    min = s * (30/100)
    prestacao = round(p / (a * 12), 2)
    print(f'Para pagar uma casa de {p}R$ em {a} anos,', end='')
    print(f' a Prestação será de {prestacao}R$')
    return min >= prestacao

main()