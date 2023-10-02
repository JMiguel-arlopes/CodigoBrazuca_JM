"""Verifica se possui 'Lopes' em seu nome"""

def main():
    name = input('Qual seu Nome? ').strip()
    response = verificador(name)
    print(f'Seu nome possui Lopes? {response}')


def verificador(name):
    response = 'lopes'
    return response in name.lower()

main()