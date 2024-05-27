import tron_interface
import util
from tron_interface import TronInterface
from btc_interface import BitcoinInterface

VERSION = "0.1"

tron = TronInterface()
bitcoin = BitcoinInterface()

terminated = False

commands_context = {
    "q": "q - quit",
    "r": "r - readme",
    "c": "c - switch coin."
}

coins = ["TRX","BTC"]
coin_index = 0

def terminate():
    terminated = True

def info():
    util.print_shelf()
    print("this script is for simple transaction broadcasting, so monitor blockchain yourself.")
    print("you must also keep track of your account's energy before sending USDT.")
    print("remember that sending USDT to account that does not have USDT costs double energy.")
    print("energy for USDT transaction can be rented from any tron energy renting service.")
    print("if you leave fee limit empty it will be set to 20 trx by default.")
    util.print_shelf()

def switch_coin():
    global coin_index
    coin_index += 1
    if (coin_index >= len(coins)):
        coin_index = 0

commands = {
    "q": terminate,
    "r": info,
    "c": switch_coin
}

def input_menu():
    print("commands:")

    if (coins[coin_index] == "TRX"):
        for i in tron.commands:
            ctx = tron.commands_context[i]
            print("> " + ctx)
    if (coins[coin_index] == "BTC"):
        for i in bitcoin.commands:
            ctx = bitcoin.commands_context[i]
            print("> " + ctx)

    for i in commands:
        ctx = commands_context[i]
        print("> " + ctx)

    return str.strip(input())

util.print_shelf()
util.print_color("[middleman v" + VERSION + "]","BLUE")

while(not terminated):
    msg = input_menu()

    coin_cmd = None

    if (coins[coin_index] == "TRX"):
        coin_cmd = tron.commands.get(msg)
    elif (coins[coin_index] == "BTC"):
        coin_cmd = bitcoin.commands.get(msg)
    
    maincmd = commands.get(msg)

    if coin_cmd != None: 
        try:
            coin_cmd()
        except Exception as e:
            for a in e.args:
                util.print_color(a, "RED")
            util.print_color("[middleman] an error occured, try again.", "RED")
    elif maincmd != None: 
        maincmd()
    else: 
        print("[middleman] unrecognized command, try again.")