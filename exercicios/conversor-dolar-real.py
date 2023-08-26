import requests

def main():
    quantia = float(input('Quando em dólares você deseja converter para real? '))
    cotacao = api()
    print(f"a Conversão de {quantia} USD é equivalente a {round(quantia * cotacao, 2)}R$")


def api():
    response = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
    data =  response.json()
    cotacao = float(data["USDBRL"]["bid"])
    return cotacao

main()
