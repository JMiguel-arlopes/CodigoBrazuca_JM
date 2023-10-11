import csv
import PySimpleGUI as py

def main():
    while True:
        count = int(input("Insira o número da ação desejada: \n (1) - Ler nomes do arquivo \n (2) - pôr um nome a lista \n (3) - Apagar um nome do arquivo \n (4) - Finalizar sessão\n"))
        match count:
            case 1:
                read_file()
            case 2:
                incluir_nome()
            case 3:
                excluir_nome()
            case 4:
                break

def read_file():
    names = []
    with open("take.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            item = row.pop(0)
            names.append(item)
         
    return names

def incluir_nome(name):
    # name = str(input("Qual nome deseja inserir: "))
    data = name.strip()
    with open("take.csv", "a") as file:
        file.write(data + "\n")

def excluir_nome(name):
    names = []
    data = name.strip()
    # name = str(input('nome para apagar: '))

    with open("take.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            item = row.pop(0)
            names.append(item)

        if data in names:
            names.remove(data)
        else:
            print('O nome não está na lista')

    with open("take.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name"])
        for row in names:
            writer.writerow({"name": row})

py.theme('DarkAmber')

layout = [  
    [py.Text('po não sei exatamente')],
    [py.Button('Inserir nome ao arquivo'), py.InputText(key="inserir")],
    [py.Button('Apagar nome do arquivo'), py.InputText(key="delete")],
    [py.Button('Ler nomes')],
    # read_file(),
]

window = py.Window('Confere palavras CSV', layout)

while True:
    event, values = window.read()

    if event == 'Ler nomes':
        nice = map(str, [1, 2, 3])
        name = ", ".join(nice)

        kk = int("1, 2, 3")
        print(kk)
        # print(name)
        result = name.strip("'")
        # py.popup(result)
        # read_file()
        # window = py.Window('Confere palavras CSV', layout)

    if event == 'Inserir nome ao arquivo':
        value = values['inserir']
        incluir_nome(value)

    if event == 'Apagar nome do arquivo':
        value = values['delete']
        excluir_nome(value)

    if event == py.WIN_CLOSED or event == 'Cancel':
        break
        
window.close()


# main()