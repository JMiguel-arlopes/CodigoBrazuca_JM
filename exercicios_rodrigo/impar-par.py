def main():
    num = int(input('Digite um número qualquer: '))
    result = verificador(num)
    print(f'O número {num} é {result}')

def verificador(num):
    return 'Par' if num % 2 == 0 else 'Impar'
        
main()