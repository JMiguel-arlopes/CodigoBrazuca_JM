def main(): 
    num = int(input('Escolha um Número: '))
    results = tabuada(num)
    for i, n in enumerate(results):
        print(f'{num} x {i+1} = {n}')
    
def tabuada(n):
    count = 1
    lista = []
    while count <= 10:    
        lista.append(n * count)
        count += 1

    return lista

main()
