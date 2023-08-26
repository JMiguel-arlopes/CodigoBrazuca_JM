def main():
    salario = float(input('Qual o seu salário atual? '))
    valor = reajuste(salario)
    print("---------------------------------------------------------------------------------------")
    print('RESULT:')
    print(f'Devido sua alta produtividade, seu salário de {salario}R$ você ganhou um aumento de 20%, ficando agora com {valor}R$')
    print("---------------------------------------------------------------------------------------")

def reajuste(x):
    return x + (x * (20/100))

main()