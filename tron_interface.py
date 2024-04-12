from typing import Any
from tronpy import Tron
from tronpy.tron import Transaction
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider
import requests
import util
import json


class TronInterface:
    def __init__(self):
        self.tron = Tron(HTTPProvider("https://api.trongrid.io",60,["273ea69b-c387-46cd-bc39-879c22a347a9"]))
        self.TRONSCAN_API_URL = "https://apilist.tronscan.org/api/account"
        self.commands = {
        "1": self.send_trx,
        "2": self.send_usdt,
        "4": self.unfreeze_balance,
        }
        self.commands_context = {
            "1": "1 - send trx",
            "2": "2 - send usd",
            "4": "4 - unfreeze balance"
        }

    def collect_userinput_details(self, args):
        inputs = {}
        
        util.print_shelf()
        print("[Details]")
        for i in args:
            inputs[i] = str.strip(input("> {}: ".format(i)))

        util.print_shelf()
        yn = str.strip(util.input_color("proceed? [y/n]: ","YELLOW"))

        if (yn == "y"):
            return inputs
        
        util.print_color("[middleman] procedure cancelled by user.", "RED")
        return None
    

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
        #details = self.collect_userinput_details(["KEY","ADDRESS", "AMOUNT_TRX"])

        details = {
            "KEY": "5a9007e0d8f54dc973fa985b141b40d4f69652140c4f1d6db2b78addf39df936",
            "ADDRESS": "TS6hTJ8CHGd9hoYF2FgoPRsVLJNVfKqfAR",
            "AMOUNT_TRX": "0.25"
        }

        if details == None:
            return None
        
        ##custom_fee = util.input_color("custom fee (empty = use energy instead): ")

        util.print_color("type coconut to confirm transaction:", "GREEN")

        str_pvk = details["KEY"]
        private_key = PrivateKey(bytes.fromhex(str_pvk))
        str_sender_address = private_key.public_key.to_base58check_address()
        str_recipient_address = details["ADDRESS"]
        str_amount = details["AMOUNT_TRX"]
        str_coin = "TRX"

        tx = (self.tron.trx.transfer(str_sender_address, str_recipient_address,5_000_000).build().sign(private_key))
        response = tx.broadcast().wait()

        util.print_color(str(response),"YELLOW")

    def send_usdt(self):
        str_pvk = str.strip(input("private key: "))
        str_add = str.strip(input("address: "))
        str_amount = str.strip(input("amount: "))

        util.print_shelf()
        print("Details:")
        print("> KEY: " + str_pvk)
        print("> RECIPIENT: " + str_add)
        print("> USDT: " + str_amount)
        util.print_shelf()
        util.print_color("type coconut to confirm transaction:")

    def unfreeze_balance(self):
        details = self.collect_userinput_details(["KEY","RESOURCE","AMOUNT"])

        if not details:
            return None 

        str_pvk = details["KEY"]
        private_key = PrivateKey(bytes.fromhex(str_pvk))
        address = private_key.public_key.to_base58check_address()
        resource = str.upper(details["RESOURCE"])

        # payload = {"address": address}
        # response = requests.get(self.TRONSCAN_API_URL, params=payload)
        # data = response.json()
        # frozen = data["frozen_balance"]
        tx = (self.tron.trx.unfreeze_balance(owner=address,resource=resource,unfreeze_balance=int(details["AMOUNT"])).build().sign(private_key))
        response = tx.broadcast().wait()
        print(response)


