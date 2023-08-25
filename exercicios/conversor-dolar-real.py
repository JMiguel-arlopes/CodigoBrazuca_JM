import requests

response = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')
data = response.json()
cotacao = float(data["USDBRL"]["bid"])
print(cotacao)

quantia = float(input('Quando em dólares você deseja converter para real? '))

print(f"a Conversão de {quantia} USD é equivalente a {quantia * cotacao}R$")

