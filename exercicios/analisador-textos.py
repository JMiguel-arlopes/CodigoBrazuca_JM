def main():
    nome =  input('Insira seu Nome: ')
    result = analisador(nome)

    up = result[0]
    lw = result[1]
    size = result[2]

    print(f'Seu nome em maiúsculo é {up}')
    print(f'Seu nome em minúsculo é {lw}')
    print(f'O tamanho do seu nome possui {size} caracteres')



def analisador(nome):
    up = nome.upper()
    lw = nome.lower()
    size = len(nome) - nome.count(' ')

    return [up, lw, size]

main()