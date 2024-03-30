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

strAddress = input("Recipient Address:")
strAddress = str.strip(strAddress)

strAmount = input("Amount to send:")
strAmount = str.strip(strAmount)
#strPrivKey = "3d6cad5fe058775fed79fe2d8cf5d302751b7aacb5fd0bd960daadec842d1a58"
#strAddress = "TGk7fukQ1qR291wM8SnsHdA7PTWqbsUmB8"
#strAmount = 100

print("--------------------------------")
print("[Details]")
print("> Private key: " + strPrivKey)
print("> Recipient Address: " + strAddress)
print("> Amount to send: " + strAmount)
print("--------------------------------")
strFinal = input("type coconut to confirm transaction: ")

if strFinal == "coconut":
    try:
        
        private_key = PrivateKey(bytes.fromhex(strPrivKey))
        address = private_key.public_key.to_base58check_address()
        token_address = "TR7NHqjeKQxGTCi8q8ZY4pL8otSzgjLj6t"  # USDT contract address on Tron mainnet
        recipient_address = strAddress
        amount = int(strAmount)  # Amount of USDT to send (in decimal format)
        amount_in_wei = int(amount * 10 ** 6)  # Convert to USDT's decimal precision (6 decimals)

        token_contract = tron.get_contract(token_address)

        tx = (
            token_contract.functions.transfer(
                recipient_address,
                amount)
            .with_owner(address)
            #.fee_limit(5_000_000)
            .build()
            .sign(private_key)
        )
        print("> details confirmed, broadcasting transaction.")
        response = tron.broadcast(tx).wait()
        print("> transaction successful.")
    except Exception as e:
        print(e)
        print("> transaction failed: error occured.")
else:
    print("> transaction failed: cancelled by user.")
