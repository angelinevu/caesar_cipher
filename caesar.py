ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Encrypt according to a string alphabet
def encrypt(plainText, key):
    encryption = ''                            #Resulting encryption
    for j in range(0, len(plainText)):         #Cycle through string
        for k in range(0, len(ALPHABET)):      #Cycle through string
            if plainText[j].upper() == ALPHABET[k] and plainText[j] != ' ':
                index = int(k + key)            
                index = index % len(ALPHABET)
                encryption += ALPHABET[index]  #Add char
                break
    return encryption

#Decrypt according to a string alphabet
def decrypt(cipherText, key):
    decryption = ''                             #Resulting decryption
    for j in range(0, len(cipherText)):         #Cycle through string
        for k in range(0, len(ALPHABET)):       #Cycle through alphabet
            if cipherText[j].upper() == ALPHABET[k]:
                index = int(k - key)
                index = index % len(ALPHABET)
                decryption += ALPHABET[index]   #Add char
                break
    return decryption
  
#Brute Force Decryption
#Display all decodings of all keys
def brute_force(text):
    list = []
    for i in range(1, len(ALPHABET)):   #Cycle through keys
        decryption = decrypt(text, i)
        list.append(f'Key: {i} -> {decryption}')
        i += 1
    return list