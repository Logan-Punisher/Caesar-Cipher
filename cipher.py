try:
    def cipherKeyEn():
        key = input("Enter the crypto-key Number between 1 - 26 to encrypt: ")
        if key.isdigit():
            key = int(key)
            if 0 < key < 26:
                return key
            else:
                print("Enter the value between 1 - 26 to encrypt !!!!!")
                return cipherKeyEn()
        else:
            print("Entered Crypto-key is not numeric Kindly redo :-(")
            return cipherKeyEn()
except Exception:
    print("Code Exited From Backdoor Secrectly o_o")
    
try:    
    def cipherKeyDe():
        key = input("Enter the crypto-key Number between 1 - 26 to decrypt: ")
        if key.isdigit():
            key = int(key)
            if 0 < key < 26:
                return key
            else:
                print("Enter the value between 1 - 26 to decrypt !!!!!")
                return cipherKeyDe()
        else:
            print("Entered Crypto-key is not numeric Kindly redo :-(")
            return cipherKeyDe()
except KeyboardInterrupt :
    print("Code Exited From Backdoor Secrectly o_o")
#cipherKey()