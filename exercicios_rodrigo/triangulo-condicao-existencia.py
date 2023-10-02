def main():
    sides = side()
    LA, LB, LC = sides
    result = verificador(LA, LB, LC)

    print('-' *35)
    if result:
        type_of = triangulo(LA, LB, LC)
        print(f'Este é um Triangulo{type_of}.')
    else:
        print(f'Infelizmente os Lados {LA}, {LB} e {LC} não formam um Triângulo.')
    print('-' *35)

def side():
    lista = []
    for i in range(3):
      value = int(input(f'Digite o valor do {i+1}° Lado do Triangulo: '))
      lista.append(value)
    return lista

def verificador(LA, LB, LC):
    return LA < LB + LC and LB < LA + LC and LC < LA + LB

def triangulo(LA, LB, LC):
    if LA == LB and LA == LC:
        return 'EQUILATERO'
    elif LA == LB and LA != LC or LA == LC and LA != LB:
        return 'ISOCELES'
    elif LA != LB and LA != LC:
        return 'ESCALENO'

main()