try:
    def encryption(message,key,alpha):
        encrypted = ""
        for mcPosition in message:
            position = alpha.find(mcPosition)
            newPosition = position + int(key)
            if mcPosition in alpha:
                encrypted = encrypted + alpha[newPosition]
            else:
                encrypted = encrypted + mcPosition
        return encrypted
except KeyboardInterrupt :
    print("Code Exited From Backdoor Secrectly o_o")


"""
alpha=getDouble()
key=cipherKey()
mess=getMessage()

print(encryption(mess,key,alpha))
"""