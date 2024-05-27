
import bit.transaction
import util
import requests
import numbers
import json
from bit import PrivateKey
import bit.network

class BitcoinInterface:
    def __init__(self):
        self.commands = {
        "1": self.send_btc
        }
        self.commands_context = {
            "1": "1 - send btc"
        }
    
    def send_btc(self):
        details = util.startmenu_details_editor("Transaction", ["KEY", "ADDRESS", "AMOUNT"])
        if details == None:
            return None

        key = PrivateKey(details["KEY"])
        print("[middleman] estimating fees...")
        fee = None
        fees = requests.get("https://mempool.space/api/v1/fees/recommended").json()

        for i in fees:
            print(f"{i} - {fees[i]}")

        selected_fee = input("set custom fee? (fee/n):")

        if (selected_fee != "n"):
            fee = int(selected_fee)

        # is_fee_absolute = False;
        # if (input("is fee absolute? (y/n)") == "y"):
        #     is_fee_absolute = True

        coconut = util.input_color("Type coconut to broadcast transaction:", "GREEN")
        if coconut != "coconut":
            util.print_color("[middleman] didn't pass the coconut challenge.","YELLOW")
            return
        
        amount = details["AMOUNT"]

        key.send([(details["ADDRESS"],amount,"btc")],fee)
        util.print_color("[middleman] operation complete!","GREEN")
