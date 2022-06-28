def encrypt(text, s):
    result=" "
    for i in range(len(text)):
        ch = text[i]
        if(ch.isupper()):
            result += chr((ord(ch)+s-65)%26+65)
        else:
            result += chr((ord(ch)+s-65)%26+65)
    return result
text = "HEMLO"
s=3
print(text)
print(encrypt(text,s))