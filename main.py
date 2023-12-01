from cipher import cipherKeyEn , cipherKeyDe
from encrypt import encryption
from doublefunction import getDouble
from message import getMessageEn , getMessageDe
from decrypt import decryption

try:
    while True:
        userinput=int(input("Enter Which operation youe want to do:\n 1. Encryption \n 2. Decryption \n 3. Exit \n Enter your Value: "))

        if userinput == 1:
            print(encryption(message=getMessageEn(),key=cipherKeyEn(),alpha=getDouble()))
        elif userinput == 2:
            print(decryption(enmessage=getMessageDe(),key=cipherKeyDe(),alpha=getDouble()))
        elif userinput == 3:
            print("GoodBye Adios ")
            break
        else:
            print("enter Proper Value!!! ")
except KeyboardInterrupt :
    print("\n Code Exited From Backdoor Secrectly o_o")
