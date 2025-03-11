import json
import os
import datetime

stock_file = "stock.json"
stock = []
saldo = 0
moedas_possiveis = {
        "5c": 0.05, 
        "10c": 0.10, 
        "20c": 0.20, 
        "50c": 0.50, 
        "1e": 1.00, 
        "2e": 2.00
}


def load_stock():
    global stock
    
    with open("stock.json", 'r') as file:
        stock = json.load(file)


def save_stock():
    with open(stock_file, 'w') as file:
        json.dump(stock, file, indent=4)


def list_products():
    print("maq:")
    print("cod | nome | quantidade | preço")
    print("---------------------------------")
    for produto in stock:
        print(f"{produto['cod']} {produto['nome']} {produto['quant']} {produto['preco']}")


def insert_saldo(moedas):
    global saldo

    moedas_string = moedas.replace("MOEDA ", "").replace(".", "").replace(" ", "").split(",")
    for moeda in moedas_string:
        if moeda in moedas_possiveis:
            saldo += moedas_possiveis[moeda]


def convert_value(value):
    euros = int(value)
    centimos = int((value - euros) * 100)
    if euros == 0:
        return f"{centimos}c"
    else:
        return f"{euros}e{centimos}c"


def show_saldo():
    print(f"maq: Saldo = {convert_value(saldo)}")


def select_product(code):
    global saldo, stock
    product = None

    for prod in stock:
        if prod['cod'] == code:
            product = prod
            break

    if product is None:
        print(f"Produto não existe")
        return
    
    if product['quant'] == 0:
        print(f"Produto esgotado")
        return
    
    if product['preco'] >= saldo:
        print("maq: Saldo insuficiente para satisfazer o seu pedido")
        print(f"maq: Saldo = {convert_value(saldo)}; Pedido = {convert_value(product['preco'])}")
        return
    
    product['quant'] -= 1
    saldo -= product['preco']
    print(f"maq: Pode retirar o produto dispensado {product['nome']}")
    show_saldo()


def get_troco():
    global saldo, moedas_possiveis

    if saldo == 0:
        return "0c"
    
    moedas_troco = {}
    saldo_temp = saldo

    valores_moedas = sorted([(valor, nome) for nome, valor in moedas_possiveis.items()], reverse=True)
    
    for valor, nome in valores_moedas:
        if saldo_temp >= valor:
            quantidade = int(saldo_temp // valor)
            saldo_temp %= valor
            moedas_troco[nome] = quantidade
    
    resultado = []
    for moeda, quant in moedas_troco.items():
        if quant > 0:
            resultado.append(f"{quant}x {moeda}")
    
    return ", ".join(resultado)


def process_exit():
    global saldo
    if saldo > 0:
        troco = get_troco()
        print(f"maq: Pode retirar o troco: {troco}.")
        saldo = 0


def main():
    load_stock()
    print(f"maq: {datetime.date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    while True:
        command = input(">> ")
    
        
        if command == "LISTAR":
            list_products()
        elif command.startswith("MOEDA "):
            moedas = command.replace("MOEDA ", "").strip()
            insert_saldo(moedas)
            show_saldo()
        elif command.startswith("SELECIONAR "):
            code = command.replace("SELECIONAR ", "")
            select_product(code)
        elif command == "SAIR":
            process_exit()
            print("maq: Até à próxima")
            save_stock()
            break
        else:
            print("O comando que introduziu é inválido.")



if __name__ == "__main__":
    main()