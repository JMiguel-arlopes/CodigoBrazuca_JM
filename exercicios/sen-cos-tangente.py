from math import radians, sin, cos, tan

def main():
    deg = float(input('Qual o ângulo que você deseja: '))
    seno = round(sen(deg), 3)
    cosseno = round(coss(deg), 3)
    tangente = round(tang(deg), 3)

    print('------------------------------------------------------')
    print(f'O Seno desse ângulo é {seno}')
    print(f'O Cosseno desse ângulo é {cosseno}')
    print(f'A tangente desse ângulo é {tangente}')
    print('------------------------------------------------------')

def sen(deg):
    return sin(radians(deg))

def coss(deg):
    return cos(radians(deg))

def tang(deg):
    return tan(radians(deg))

main()