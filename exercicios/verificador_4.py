def main():
    """DIz quantas vees aparece a letra 'A', a primeira e ultima posição dela"""
    # ideia: faça o usuario escolher qual letra ele quer identificar.
    name = input('Digite um Nome Qualquer: ').strip().lower()
    count_letter = count(name)
    first_letter = first(name)
    last_letter = last(name)

    print('---------------------------------------------------')
    print(f'A letra "A" apareceu {count_letter} Vezes')
    print(f'A primeira Letra "A" está na posição {first_letter}')
    print(f'A última Letra "A" está na posição {last_letter}')
    print('---------------------------------------------------')

def count(name):
    return name.count('a')

def first(name):
    return name.find('a')+1

def last(name):
    return name.rfind('a')+1

main()