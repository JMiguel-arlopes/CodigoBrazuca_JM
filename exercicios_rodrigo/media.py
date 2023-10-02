def main():
    size = int(input('Digite qauntas notas você tem: '))
    notas = listagem(size)
    total = sum(notas)
    mediaPronta = media(total, len(notas))
    
    print('-' *35)
    print(f'Dentre suas notas {notas}')
    print('Sua média é', mediaPronta)
    print('-' *35)

def listagem(size):
    lista = []
    for i in range(size):
        num = int(input(f'Digite sua {i+1} Nota: '))
        lista.append(num)
    return lista

def media(total, lista):
    return total/lista

main()