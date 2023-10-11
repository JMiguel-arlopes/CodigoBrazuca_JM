# Faça um script que permita o uso de 2 argparsers ("AGE", CITY) 
# se for passado idade/cidade então printe na tela o valor. Se não, printe
# "nenhuma mensagem fornecida"

from argparse import ArgumentParser as AP
from sys import argv

parser = AP(description="kahsjkds")

match argv[1]:
    case "--city":
        parser.add_argument("--city", help="Digite por extenso", type=str, default="AQUI", required=False, error="koeeeee")
        args = parser.parse_args()
        print(f'A sua idade é: {args.city}')

    case "--age":
        parser.add_argument("--age", help="escreva um número inteiro", type=int, default=1)
        args = parser.parse_args()
        print(f'A sua idade é: {args.age}')

    case _:
        print('Existem apenas "--city" e "--age", especifique corretamente.')


# print(argv[1])

