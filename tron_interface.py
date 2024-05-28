from typing import Any
from tronpy import Tron
from tronpy.tron import Transaction
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider
import requests
import util
import json
import time

class TronInterface:
    def __init__(self):
        self.tron = Tron(HTTPProvider("https://api.trongrid.io",60,["273ea69b-c387-46cd-bc39-879c22a347a9"]))
        self.TRONSCAN_API_URL = "https://apilist.tronscan.org/api/account"
        self.commands = {
        "1": self.send_trx,
        "2": self.send_usdt,
        "3": self.freeze_balance,
        "4": self.unfreeze_balance
        }
        self.commands_context = {
            "1": "1 - send trx",
            "2": "2 - send usdt",
            "3": "3 - freeze balance",
            "4": "4 - unfreeze balance"
        }

    def _find_chainparam_value_by_key(self, collection, key):
         for i in collection:
            if i["key"] == key:
                return i["value"]


    def send_trx_internal(self, details):
        return None

    async def get_parameters_internal(self, details):
        params = None
        while(not params):
            try:
                params = await self.send_trx_internal(details)
            except Exception as e:
                print(e)
                print("[middleman] error occured, retrying.")
        return params
    
    def get_bytesize_internal(self, tr: Transaction):
        raw = tr._raw_data
        js = json.dumps(raw)
        hx = js.encode()
        bt = len(hx) / 2
        a = 1
        return 0

    def send_trx(self):
        details = util.startmenu_details_editor("Transaction", ["KEY", "ADDRESS", "AMOUNT_TRX_SUN", "MEMO","FEE_LIMIT"])

        if details == None:
            return None

        if details["FEE_LIMIT"] == "":
            details["FEE_LIMIT"] = 16_000_000

        coconut = util.input_color("Type coconut to broadcast transaction:", "GREEN")

        if coconut != "coconut":
            util.print_color("[middleman] didn't pass the coconut challenge.","YELLOW")
            return

        str_pvk = details["KEY"]
        private_key = PrivateKey(bytes.fromhex(str_pvk))
        str_sender_address = private_key.public_key.to_base58check_address()
        str_recipient_address = details["ADDRESS"]
        fee = int(details["FEE_LIMIT"])
        amount = int(details["AMOUNT_TRX_SUN"])

        tx = (self.tron.trx.transfer(str_sender_address, str_recipient_address,amount).memo(details["MEMO"]).fee_limit(fee).build().sign(private_key))
        responce = tx.broadcast().wait()
        print(responce)
        print("[middleman] operation finished.")

    def send_usdt(self):
        details = util.startmenu_details_editor("Transaction", ["KEY", "ADDRESS", "AMOUNT_USDT_SUN", "MEMO", "FEE_LIMIT"])

        if details == None:
            return None

        if details["FEE_LIMIT"] == "":
            details["FEE_LIMIT"] = 16_000_000

        coconut = util.input_color("Type coconut to broadcast transaction:", "GREEN")

        if coconut != "coconut":
                util.print_color("[middleman] didn't pass the coconut challenge.","YELLOW")
                return

        token_address = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # USDT contract address on Tron mainnet
        token_contract = self.tron.get_contract(token_address)

        str_pvk = details["KEY"]
        private_key = PrivateKey(bytes.fromhex(str_pvk))
        str_sender_address = private_key.public_key.to_base58check_address()
        str_recipient_address = details["ADDRESS"]
        amount = int(details["AMOUNT_USDT_SUN"])
        fee = int(details["FEE_LIMIT"])

        tx = (token_contract.functions.transfer(str_recipient_address,amount)
              .with_owner(str_sender_address)
              .fee_limit(fee)
              .memo(details["MEMO"])
              .build()
              .sign(private_key))
        responce = tx.broadcast()
        print(responce)
        print("[middleman] operation finished.")

    def freeze_balance(self):
        details = self.collect_userinput_details(["KEY","RESOURCE","AMOUNT"])

        if not details:
            return None 

        str_pvk = details["KEY"]
        private_key = PrivateKey(bytes.fromhex(str_pvk))
        address = private_key.public_key.to_base58check_address()
        resource = str.upper(details["RESOURCE"])
        amount = int(details["AMOUNT"])

        tx = (self.tron.trx.freeze_balance(owner=address,amount=amount,resource=resource).build().sign(private_key))
        tx.broadcast()
        util.print_color("[middleman] operation complete!","GREEN")

    def unfreeze_balance(self):
        details = self.collect_userinput_details(["KEY","RESOURCE","AMOUNT"])

        if not details:
            return None 

        str_pvk = details["KEY"]
        private_key = PrivateKey(bytes.fromhex(str_pvk))
        address = private_key.public_key.to_base58check_address()
        resource = str.upper(details["RESOURCE"])
        amount = int(details["AMOUNT"])
        
        tx = (self.tron.trx.unfreeze_balance(owner=address,resource=resource,unfreeze_balance=amount).build().sign(private_key))
        tx.broadcast()
        util.print_color("[middleman] operation complete!","GREEN")




