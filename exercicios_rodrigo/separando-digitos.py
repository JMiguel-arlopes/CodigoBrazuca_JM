def main():
    # Ideia de upgrade: faça uma lista com o nome das casas decimais e depois faça um
    # ForLoop onde o index representa a posição do item tanto na lista dos valores,
    # quanto na lista de casas decimais
    num = int(input('Digite um número inteiro na casa dos Milhares: '))
    valor = separador(num)
    print('----------------------------')
    print('Para o número')
    print(f'o Valor do Milhar é {valor[3]}')
    print(f'o Valor da Centana é {valor[2]}')
    print(f'o Valor da Dezena é {valor[1]}')
    print(f'o Valor da Unidade é {valor[0]}')
    print('----------------------------')
    

def separador(num):
    lista = []

    for i in range(len(str(num))):
        if not lista:
            lista.append(num % 10)
        else:
            n = int(num / (10**i) % 10)
            lista.append(n)

    return lista

main()

        
        