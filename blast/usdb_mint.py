import configparser
from web3 import Web3

config = configparser.ConfigParser()
config.read("config.properties")

# Initialize the address calling the functions/signing transactions
caller = config.get("key","wallet_addy")
private_key = config.get("key","wallet_priv_key")  # To sign the transaction

# Initialize endpoint URLa
node_url = "https://nd-423-241-025.p2pify.com/ad7939def28bc9627b64dcf581ae3b3f"   

def call_mint():
    # Create the node connection
    web3 = Web3(Web3.HTTPProvider(node_url))

    # Verify if the connection is successful
    if web3.is_connected():
        print("-" * 50)
        print("Connection Successful")
        print("-" * 50)
    else:
        print("Connection Failed")

    # Initialize address nonce
    nonce = web3.eth.get_transaction_count(caller)

    # Initialize contract ABI and address, an ERC20 token ABI in this case
    abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]'

    contract_address = "0x7f11f79DEA8CE904ed0249a23930f2e59b43a385"   #USDB mint

    # Create smart contract instance
    contract = web3.eth.contract(address=contract_address, abi=abi)

    # initialize the chain id, we need it to build the transaction for replay protection
    Chain_id = web3.eth.chain_id

    #function param
    addr_to = '0x696969BB7738e18A9108562b2120F82414c8B12A'
    amount = 10000000000000000000000

    print("Minting USDB...")
    for i in range(5):
        # Call the mint function passing addr_to, amount as a parameter
        call_function = contract.functions.mint(addr_to,amount).build_transaction({"chainId": Chain_id, "from": caller, "nonce": nonce})

        # Sign transaction
        signed_tx = web3.eth.account.sign_transaction(call_function, private_key=private_key)
        
        # Send transaction
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        # Wait for transaction receipt
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        tx_hash = tx_receipt['transactionHash'].hex()
        print("tx hash: " + tx_hash)
        
        #get next nonce
        nonce = web3.eth.get_transaction_count(caller)


    bal = contract.functions.balanceOf(addr_to).call() 
    print(f'USDB Balance: {bal}')   
    return 0

if __name__ == '__main__':
    call_mint()