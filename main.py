import PySimpleGUI as sg
from shop import Shop, Computer

sg.theme('DarkAmber')

layout = [
    [sg.Text('Ievadiet produkta nosaukumu', size=(25, 1)), sg.InputText(key='-PNAME-')],
    [sg.Radio("Detaļa", "tips", key='-DETALA-', default=True), sg.Radio("Programmatūra", "tips", key='-PROGRAMMATURA-')],
    [sg.Text('Ievadiet produktu skaitu', size=(25, 1)), sg.InputText(key='-AMOUNT-')],
    [sg.Text('Ievadiet produktu cenu', size=(25, 1)), sg.InputText(key='-PRICE-')],
    [sg.Text('Ievadiet produktu nosaukumu rediģēšanai', size=(25, 1)), sg.InputText(key='-ENAME-')],
    [sg.Text("Produkti")],
    [sg.Output(size=(50, 10), font=('Arial', 12), key='outputt')],
    [sg.Button('Pievienot produktu'), sg.Button('Piegādāt produktus'), sg.Button('Pārdot produktus'), sg.Button('Rediģēt datus'), sg.Button('Beigt')]
]

window = sg.Window('Produktu pārvalde', layout)

products = []
total_earnings = 0

while True:
    event, values = window.read()
    window.FindElement('outputt').Update('')

    if event == sg.WIN_CLOSED or event == 'Beigt':
        break
    elif event == 'Pievienot produktu':
        product_type = 'detala' if values['-DETALA-'] else 'programmatūra'
        product = Shop(values['-PNAME-'], int(values['-AMOUNT-']), product_type, float(values['-PRICE-']))
        products.append(product)
        sg.popup(f"Produkts '{product.name}' ir veiksmīgi pievienots!")

    elif event == 'Piegādāt produktus':
        ename = values['-ENAME-']
        for product in products:
            if product.name == ename:
                product.shopDelivery(int(values['-AMOUNT-']))
                sg.popup(f"Produkti '{product.name}' daudzums ir atjaunināts!")

    elif event == 'Pārdot produktus':
        ename = values['-ENAME-']
        for product in products:
            if product.name == ename:
                amount_to_sell = int(values['-AMOUNT-'])
                sold, earnings = product.sellProduct(amount_to_sell)
                total_earnings += earnings
                sg.popup(f"Pārdoti {sold} produkti '{product.name}', ienākumi: {earnings:.2f} EUR")

    elif event == 'Rediģēt datus':
        ename = values['-ENAME-']
        for product in products:
            if product.name == ename:
                if values['-PNAME-']:
                    product.changeName(values['-PNAME-'])
                if values['-AMOUNT-']:
                    product.changeAmount(int(values['-AMOUNT-']))
                if values['-DETALA-']:
                    product.changeType('detala')
                else:
                    product.changeType('programmatūra')
                if values['-PRICE-']:
                    product.changePrice(float(values['-PRICE-']))
                sg.popup(f"Dati par produktu '{product.name}' ir veiksmīgi rediģēti!")

    for i, product in enumerate(products):
        product.printShop(i)
    
    sg.popup(f"Kopējie ienākumi: {total_earnings:.2f} EUR")

window.close()
