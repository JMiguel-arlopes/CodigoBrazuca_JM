def main():
    m = float(input('Insira uma medida em Metros: '))

    dict = conversor(m)

    print(f'\n{m} Metros equivale a:')
    for i in dict:
        print('{}{}'.format(dict[i], i.lower()), sep='')

    # print('Km')

def conversor(m):
    km = m / 1000
    hm = m / 100
    dam = m / 10
    dm = m * 10
    cm = m * 100
    mm = m * 1000

    return {
        "km": km,
        "hm": hm,
        "dam": dam,
        "dm": dm,
        "cm": cm,
        "mm": mm
    }

main()