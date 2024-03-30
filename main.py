from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider

full_node = HTTPProvider("https://api.trongrid.io")
solidity_node = HTTPProvider("https://api.trongrid.io")
event_server = HTTPProvider("https://api.trongrid.io")
tron = Tron(full_node)

print("[You are about to transfer USDT on TRON network]")

strPrivKey = input("Private key:")
strPrivKey = str.strip(strPrivKey)

strAddress = input("Recepient Address:")
strAddress = str.strip(strAddress)

strAmount = input("Amount to send:")
strAmount = str.strip(strAmount)

print("--------------------------------")
print("[Details]")
print("> Private key: " + strPrivKey)
print("> Recepient Address: " + strAddress)
print("> Amount to send: " + strAmount)
print("--------------------------------")
strFinal = input("type coconut to confirm transaction: ")

if strFinal == "coconut":
    try:
        print("> transaction confirmed.")
        private_key = PrivateKey(bytes.fromhex(strPrivKey))
        address = private_key.public_key.to_base58check_address()
        token_address = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # USDT contract address on Tron mainnet
        recipient_address = strAddress
        amount = int(strAmount)  # Amount of USDT to send (in decimal format)
        amount_in_wei = int(amount * 10 ** 6)  # Convert to USDT's decimal precision (6 decimals)

        token_contract = tron.get_contract(token_address)
        transaction = token_contract.functions.transfer(recipient_address, amount_in_wei).build_transaction(
            owner_address=address
        )
   
        signed_txn = tron.trx.sign(transaction, private_key)
        response = tron.trx.broadcast(signed_txn)
        print(response)
    except Exception as e:
        if hasattr(e, "message"):
            print(e.message)
        print("> transaction failed due to error.")
else:
    print("> transaction failed: cancelled by user.")
