from web3 import Web3

# Ganti dengan endpoint Infura atau node lain kamu
INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"

w3 = Web3(Web3.HTTPProvider(INFURA_URL))

# Private key kamu (JANGAN SEBARKAN)
PRIVATE_KEY = "YOUR_PRIVATE_KEY"
SENDER_ADDRESS = "0xYourSenderAddress"

def send_eth_transaction(to_address, amount_eth):
    try:
        nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)
        tx = {
            'nonce': nonce,
            'to': to_address,
            'value': w3.toWei(amount_eth, 'ether'),
            'gas': 21000,
            'gasPrice': w3.toWei('50', 'gwei')
        }

        signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)
        print(f"Transaksi berhasil dikirim. Tx Hash: {w3.toHex(tx_hash)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    to = input("Alamat tujuan (0x...): ").strip()
    amount = float(input("Jumlah ETH yang dikirim: "))
    if w3.isAddress(to):
        send_eth_transaction(to, amount)
    else:
        print("Alamat tujuan tidak valid.")
