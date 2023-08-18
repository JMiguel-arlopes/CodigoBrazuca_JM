def main():
    jm = input('Digite alguma coisa: ')
    classificacoes(jm)

def classificacoes(jm):
    print('JM é classificada como', type(jm))
    print('JM só obtém espaços? ', jm.isspace())
    print('É um numero? ', jm.isnumeric())
    print('É um alfabeto? ', jm.isalpha())
    print('É um alfanumerico? ', jm.isalnum())
    print('ESTÁ EM MAISCULO? ', jm.isupper())
    print('está em minúsculo? ', jm.islower())
    print('Está capitalizada? ', jm.istitle())

main()