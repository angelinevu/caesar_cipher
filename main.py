from caesar import encrypt, decrypt, brute_force

#Main function
def main():
    print('Caesar Cipher Console')
    repeat = True
    while repeat:
        print('\nCipher menu:\n\n\t1. Encrypt a Message\n\t2. Decrypt a Message\n\t3. Exit')
        option = float(input('\nSelect an option: '))
            
        if option == 1:     #Encryption
            text = input('\nEnter Plain Text: ')
            key = float(input('Enter a key value (1-26): '))
            encryption = encrypt(text, key)
            print(f'\nEncryption: {encryption}')
        
        if option == 2:     #Decryption
            text = input('\nEnter Cipher Text: ')
            key = int(input('Enter a key value (1-26): '))
            decryption = decrypt(text, key)
            print(f'\nDecryption: {decryption}')
            
        if option == 3:     #Quit
            repeat = False
            print('Program Exited')
            
        if option == 99:    #Special feature
            print('\nCommence Brute Force Attack')
            text = input('\nEnter Cipher Text: ')
            results = brute_force(text)
            i = 0
            for i in range(0, len(results)):
                print(results[i])

if __name__ == "__main__":
    main()