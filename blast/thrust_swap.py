import sys
from web3 import Web3
from hexbytes import HexBytes

# Initialize endpoint URL
node_url = "https://nd-423-241-025.p2pify.com/ad7939def28bc9627b64dcf581ae3b3f"


# Initialize contract ABI and address, an ERC20 token ABI in this case
abi = '[{"inputs":[{"internalType":"address","name":"_factory","type":"address"},{"internalType":"address","name":"_WETH9","type":"address"},{"internalType":"address","name":"_manager","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"recipient","type":"address"},{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"ClaimGas","type":"event"},{"inputs":[],"name":"BLAST","outputs":[{"internalType":"contract IBlast","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"WETH9","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_recipient","type":"address"},{"internalType":"uint256","name":"_minClaimRateBips","type":"uint256"}],"name":"claimGas","outputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"components":[{"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"}],"internalType":"struct ISwapRouter.ExactInputParams","name":"params","type":"tuple"}],"name":"exactInput","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountIn","type":"uint256"},{"internalType":"uint256","name":"amountOutMinimum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactInputSingleParams","name":"params","type":"tuple"}],"name":"exactInputSingle","outputs":[{"internalType":"uint256","name":"amountOut","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"bytes","name":"path","type":"bytes"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMaximum","type":"uint256"}],"internalType":"struct ISwapRouter.ExactOutputParams","name":"params","type":"tuple"}],"name":"exactOutput","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[{"components":[{"internalType":"address","name":"tokenIn","type":"address"},{"internalType":"address","name":"tokenOut","type":"address"},{"internalType":"uint24","name":"fee","type":"uint24"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint256","name":"amountOut","type":"uint256"},{"internalType":"uint256","name":"amountInMaximum","type":"uint256"},{"internalType":"uint160","name":"sqrtPriceLimitX96","type":"uint160"}],"internalType":"struct ISwapRouter.ExactOutputSingleParams","name":"params","type":"tuple"}],"name":"exactOutputSingle","outputs":[{"internalType":"uint256","name":"amountIn","type":"uint256"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"factory","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"manager","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes[]","name":"data","type":"bytes[]"}],"name":"multicall","outputs":[{"internalType":"bytes[]","name":"results","type":"bytes[]"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"refundETH","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowed","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitAllowedIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"value","type":"uint256"},{"internalType":"uint256","name":"deadline","type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"selfPermitIfNecessary","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"_manager","type":"address"}],"name":"setManager","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"sweepToken","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"token","type":"address"},{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"feeBips","type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],"name":"sweepTokenWithFee","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"int256","name":"amount0Delta","type":"int256"},{"internalType":"int256","name":"amount1Delta","type":"int256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"thrusterSwapCallback","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"}],"name":"unwrapWETH9","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amountMinimum","type":"uint256"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"feeBips","type":"uint256"},{"internalType":"address","name":"feeRecipient","type":"address"}],"name":"unwrapWETH9WithFee","outputs":[],"stateMutability":"payable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

contract_address = "0xE4690BD7A9cFc681A209443BCE31aB943F9a9459"   #Thrust Swap


# Initialize the address calling the functions/signing transactions
caller = "<wallet addy>"
private_key = ""  # To sign the transaction

data = "0xac9650d80000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000124c04b8d59000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000005138cb94d86d6cde09c491fd72c81095c965bf010000000000000000000000000000000000000000000000000000000065de830c00000000000000000000000000000000000000000001a784457e508ee9640000000000000000000000000000000000000000000000001a773cb8b484a3975e6d000000000000000000000000000000000000000000000000000000000000002b4200000000000000000000000000000000000022000bb8f6d86a117b761ec5e441ed8c3b190dbda745623e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
data_bytes = Web3.to_bytes(hexstr=data)

""" data_bytes = [HexBytes('0000000000000000000000000000000000000000000000000000000000000020'),
HexBytes('0000000000000000000000000000000000000000000000000000000000000001'),
HexBytes('0000000000000000000000000000000000000000000000000000000000000020'),
HexBytes('0000000000000000000000000000000000000000000000000000000000000124'),
HexBytes('c04b8d5900000000000000000000000000000000000000000000000000000000'),
HexBytes('0000002000000000000000000000000000000000000000000000000000000000'),
HexBytes('000000a00000000000000000000000005138cb94d86d6cde09c491fd72c81095v'),
HexBytes('c965bf0100000000000000000000000000000000000000000000000000000000'),
HexBytes('65de830c00000000000000000000000000000000000000000001a784457e508e'),
HexBytes('e9640000000000000000000000000000000000000000000000001a773cb8b484'),
HexBytes('a3975e6d00000000000000000000000000000000000000000000000000000000'),
HexBytes('0000002b4200000000000000000000000000000000000022000bb8f6d86a117b'),
HexBytes('761ec5e441ed8c3b190dbda745623e0000000000000000000000000000000000'),
HexBytes('0000000000000000000000000000000000000000000000000000000000000000')] """

data_bytes = bytearray("0xac9650d80000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000124c04b8d59000000000000000000000000000000000000000000000000000000000000002000000000000000000000000000000000000000000000000000000000000000a00000000000000000000000005138cb94d86d6cde09c491fd72c81095c965bf010000000000000000000000000000000000000000000000000000000065de830c00000000000000000000000000000000000000000001a784457e508ee9640000000000000000000000000000000000000000000000001a773cb8b484a3975e6d000000000000000000000000000000000000000000000000000000000000002b4200000000000000000000000000000000000022000bb8f6d86a117b761ec5e441ed8c3b190dbda745623e00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000", 'utf-8')

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

    # Create smart contract instance
    contract = web3.eth.contract(address=contract_address, abi=abi)

    # initialize the chain id, we need it to build the transaction for replay protection
    Chain_id = '168587773'

    #function param
    addr_to = '0x696969BB7738e18A9108562b2120F82414c8B12A'
    amount = 10000000000000000000000

    print("Minting USDB...")
    for i in range(1000):
        # Call the mint function passing addr_to, amount as a parameter
        call_function = contract.functions.multicall(data_bytes).build_transaction({"chainId": Chain_id, "from": caller, "nonce": nonce})

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