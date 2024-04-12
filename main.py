import tron_interface
import util
from tron_interface import TronInterface

VERSION = "0.1"

tron_interface = TronInterface()

terminated = False

def terminate():
    terminated = True

commands = {
    "quit": terminate
}

commands_context = {
    "quit": "q - quit"
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
            util.print_color(e.args[0], "RED")
            util.print_color("[middleman] an error occured, try again.", "RED")
    elif maincmd != None: 
        maincmd()
    else: 
        print("[middleman] unrecognized command, try again.")


# if TRXOnly:
#     print("> Coin: TRX")
# else:
#     print("> Coin: USDT")
# print("--------------------------------")
# strFinal = input("type coconut to confirm transaction: ")

# if strFinal == "coconut":
#     try:
#         private_key = PrivateKey(bytes.fromhex(strPrivKey))
#         address = private_key.public_key.to_base58check_address()
#         recipient_address = strAddress
#         amount = int(strAmount)  # Amount of USDT to send (in decimal format)
#         amount_in_wei = int(amount * 10 ** 6)  # Convert to USDT's decimal precision (6 decimals)
        
#         print("> details confirmed, building transaction.")

#         if TRXOnly:
#             txn = (tron.trx.transfer(address, recipient_address, amount)
#             .build()
#             .sign(private_key))
#             response = txn.broadcast()
#         else:
#             token_address = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # USDT contract address on Tron mainnet

#             token_contract = tron.get_contract(token_address)

#             tx = (
#                 token_contract.functions.transfer(
#                     recipient_address,
#                     amount)
#                 .with_owner(address)
#                 .fee_limit(15_000_000)
#                 .build()
#                 .sign(private_key)
#             )
            
#             response = tx.broadcast()
#         print("> broadcast was successful.")
#     except Exception as e:
#         print(e)
#         print("> transaction failed: error occured.")
# else:
#     print("> transaction failed: cancelled by user.")
