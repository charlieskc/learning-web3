from eth_account import Account
import secrets
priv = secrets.token_hex(32)
private_key = "0x" + priv
print ("SAVE BUT DO NOT SHARE THIS:", private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)


## Vanity Address Example
#generate a wallet address which is start with 0x888888
while 0:
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    acct = Account.from_key(private_key)
    print("Generating Address:", acct.address)
    if str(acct.address).startswith("0x8888"):        
        print ("SAVE BUT DO NOT SHARE THIS:", private_key)
        print("Address:", acct.address)
        break



## "Special" Private key
private_key = "0x1111111111111111111111111111111111111111111111111111111111111111"

print(private_key)
acct = Account.from_key(private_key)
print("Address:", acct.address)


