from tronpy import Tron
from tronpy.keys import PrivateKey
from tronpy.providers import HTTPProvider

full_node = HTTPProvider("https://api.trongrid.io/v1")
tron = Tron(full_node)

amount = int(30)
amount_in_wei = int(amount * 10 ** 6)

pvk = PrivateKey(bytes.fromhex("5a9007e0d8f54dc973fa985b141b40d4f69652140c4f1d6db2b78addf39df936"))
address = pvk.public_key.to_base58check_address()

tx = (
    tron.trx.freeze_balance(address,amount_in_wei).build().inspect().sign(pvk).broadcast()
)
print(tx.txid)