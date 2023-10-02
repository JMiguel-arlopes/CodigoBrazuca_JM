def main():
    peso = float(input('Informe seu Peso: ').replace(',', '.'))
    altura = float(input('Informe sua altura: ').replace(',', '.'))
    imc = round(calcula_imc(peso, altura), 2)
    result = verificador(imc)

    print('-' *35)
    print(f'IMC: {imc}')
    print(f'Categoria: {result}')
    print('-' *35)

def calcula_imc(peso, altura):
    imc = peso / (altura**2)
    return imc

def verificador(imc):
    classificacoes = [
        {"indice": 18.5, "categoria": 'Abaixo do Peso'},
        {"indice": 25, "categoria": 'Peso Ideal'},
        {"indice": 30, "categoria": 'Sobrepeso'},
        {"indice": 35, "categoria": 'Obseidade'},
        {"indice": 40, "categoria": 'Obseidade Mórbida'}
    ]
    
    for classificacao in classificacoes: 
        if imc <= classificacao['indice']:
            return classificacao['categoria']
        
main()
