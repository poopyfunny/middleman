import tron_interface
import util
from tron_interface import TronInterface
import traceback

VERSION = "0.1"

tron_interface = TronInterface()

terminated = False

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

commands = {
    "q": terminate,
    "r": info
}

commands_context = {
    "q": "q - quit",
    "r": "r - readme"
}

def input_menu():
    print("commands:")

    for i in tron_interface.commands:
        ctx = tron_interface.commands_context[i]
        print("> " + ctx)

    for i in commands:
        ctx = commands_context[i]
        print("> " + ctx)

    return str.strip(input())

util.print_shelf()
util.print_color("[middleman v" + VERSION + "]","BLUE")

while(not terminated):
    msg = input_menu()
    troncmd = tron_interface.commands.get(msg)
    maincmd = commands.get(msg)
    if troncmd != None: 
        try:
            troncmd()
        except Exception as e:
            for a in e.args:
                util.print_color(a, "RED")
            util.print_color("[middleman] an error occured, try again.", "RED")
    elif maincmd != None: 
        maincmd()
    else: 
        print("[middleman] unrecognized command, try again.")