def main():
    salario = float(input('Coloque seu salário: '))

    aumento = reajuste(salario)

    print(f'Você ganhou um aumento! Seu novo salário é {aumento}R$')

def reajuste(salario):
    if salario > 2000:
        return salario + ((10/100) * salario)
    else:
        return salario + ((20/100) * salario)
    
main()