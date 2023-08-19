def main(): 
    num = int(input('Escolha um Número: '))

    for i, n in enumerate(tabuada(num)):
        print(f'{num} x {i+1} = {n}')
    

def tabuada(n):
    count = 1
    lista = []

    while True:
        if count > 10:
            return lista
        
        lista.append(n * count)
        count += 1

main()
