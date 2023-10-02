from datetime import date
def main():
    today = date.today().year
    year = int(input('Ano de Nascimento: '))
    age = today - year 
    classificacao =senioridade(age)

    print(f'O atleta tem {age} anos.')
    print(f'Classificação: { classificacao}')


def senioridade(age):
    if age >= 0 and age <= 9:
        return 'MIRIM'
    elif age <= 14:
        return 'INFANTIL'
    elif age <= 19:
        return 'JUNIOR'
    elif age <= 25:
        return 'SÊNIOR'
    elif age > 25:
        return 'MASTER'
    
main()