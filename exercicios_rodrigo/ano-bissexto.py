from datetime import date
def main():
    print('Digite "0" para dizer a data de hoje..')
    age = int(input('Digite uma data e verifique se é inteiro: '))
    age = today(age)

    print('-' * 30)
    if bissexto(age):
        print(f'{age} É um Ano Bissexto')
    else:
        print(f'{age} NÃO É um Ano Bissexto')
    print('-' * 30)

def today(age):
    if age == 0:
        age = date.today().year
    return age

def bissexto(age):
    return age % 4 == 0 and age % 100 != 0 or age % 400 == 0

main()


