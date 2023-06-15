import requests

base_url = "https://www.buda.com/api/v2/markets"

def get_bitcoin_price():
    """ This method gets the current bitcoin price in CLP """
    bitcoin_url = f"{base_url}/btc-clp/ticker"
    response = requests.get(bitcoin_url).json()['ticker']['last_price']
    print(''.join(response))
    return ''.join(response)

def buy_bitcoin(amount):
    """ This method buys bitcoin with the given amount in CLP """
    bitcoin_url = f"{base_url}/btc-clp/orders"
    price = get_bitcoin_price()

    ammount_of_bitcoin = amount / float(price.replace("CLP", "").replace(".", "").replace(",", "."))
    print(f"Se compraron {ammount_of_bitcoin} bitcoins a un precio de {price} CLP")
    return f"Se compraron {ammount_of_bitcoin} bitcoins a un precio de {price} CLP"
