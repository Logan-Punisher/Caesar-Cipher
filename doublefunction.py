import string

def getDouble():
    alpha=string.ascii_letters + string.digits + string.punctuation
    doubleAlpha = alpha + alpha
    return doubleAlpha
