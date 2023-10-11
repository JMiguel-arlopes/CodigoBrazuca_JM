# Crie um programa para rodar em "python main.py --nome (nome)" em que o argumento
# seja obrigatorio (ou requerido)

from argparse import ArgumentParser

parser = ArgumentParser(description="descricao que nao sei oq faz")
parser.add_argument("--name", required=True, default="você não me falou seu nome, mas te desculpo por isso", help="Digite apenas um nome após o --name", type=str)
args = parser.parse_args()
print(args.name)