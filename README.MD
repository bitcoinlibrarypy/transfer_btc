# Transfer BTC Script

`transfer_btc.py` is a Python script that allows you to send Bitcoin transactions by creating a wallet from a private key, creating a transaction, and broadcasting it to the Bitcoin network.

## Features
- **Create a Wallet**: Create a Bitcoin wallet from a private key.
- **Send Bitcoin**: Send Bitcoin from your wallet to any recipient address.
- **Broadcast Transactions**: Sign and broadcast transactions to the Bitcoin network.
- **Transaction Details**: Retrieve the transaction ID and raw hex data.

## Installation

### Requirements
- Python 3.x
- `pip` (Python package installer)

### Dependencies
Install required dependencies:
```bash
pip install bitcoinlib
```

## Usage

1. Modify the `transfer_btc.py` script to include your private key and recipient address:
   ```python
   private_key = "your_private_key_here"
   recipient_address = "your_recipient_bitcoin_address_here"
   amount = 100000000  # Amount in satoshis (1 BTC = 100,000,000 satoshis)
   ```

2. Run the script to send Bitcoin and print transaction details:
   ```bash
   python transfer_btc.py
   ```

### Example Output

```bash
Transaction ID: d3b2d4...9a2e6b
Transaction Hex: 0100000001...00000000
```

## Contributing

Contributions are welcome! Feel free to submit a pull request or raise an issue to improve this project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
