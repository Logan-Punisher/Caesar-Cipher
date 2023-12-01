try:
    def decryption(enmessage,key,alpha):
        decrypted=""
        #print("The Encrypted Message Is : " + enmessage)
        for Current in enmessage:   # current encrypted message position.
            position = alpha.find(Current)
            newPosition = position - int(key)
            if Current in alpha:
                decrypted = decrypted + alpha[newPosition]
            else:
                decrypted = decrypted + Current
        return decrypted
except KeyboardInterrupt :
    print("Code Exited From Backdoor Secrectly o_o")
