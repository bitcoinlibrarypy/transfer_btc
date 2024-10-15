from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction

def create_wallet_from_private_key(private_key, wallet_name="YourWalletName", network='bitcoin'):
    """
    Create a wallet from a private key.

    Args:
        private_key (str): The private key to generate the wallet from.
        wallet_name (str): The name of the wallet to be created.
        network (str): The Bitcoin network to connect to (mainnet by default).

    Returns:
        Wallet: The created wallet object.
    """
    return Wallet.create(wallet_name, keys=private_key, network=network)


def send_bitcoin(private_key, recipient_address, amount_satoshis, network='bitcoin'):
    """
    Create, sign, and send a Bitcoin transaction.

    Args:
        private_key (str): The private key associated with the wallet.
        recipient_address (str): The recipient's Bitcoin address.
        amount_satoshis (int): The amount to send in satoshis.
        network (str): The Bitcoin network (default is mainnet).

    Returns:
        dict: Transaction details including transaction ID and hex.
    """
    # Create wallet from private key
    wallet = create_wallet_from_private_key(private_key, network=network)

    # Create the transaction
    tx = Transaction.create(wallet.get_key().address, recipient_address, amount_satoshis, network=network)

    # Sign the transaction
    tx.sign()

    # Broadcast the transaction
    tx.send()

    # Return transaction details
    return {"txid": tx.txid, "hex": tx.as_hex()}


if __name__ == "__main__":
    private_key = "your_private_key_here"
    recipient_address = "your_recipient_bitcoin_address_here"
    amount = 100000000  # 1 BTC = 100,000,000 satoshis

    # Send Bitcoin and print transaction details
    transaction_details = send_bitcoin(private_key, recipient_address, amount)
    print(f"Transaction ID: {transaction_details['txid']}")
    print(f"Transaction Hex: {transaction_details['hex']}")
