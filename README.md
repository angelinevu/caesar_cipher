The program opens a menu that pops up 3 options: encryption, decryption, and exiting the program. There is a hidden option of Brute Force Attack (99).

Encryption takes in 2 inputs: text and key (integer). The program changes the text character by character. We find the character in the alphabet list and note its index. The function encrypts the text by changing the index key-value spots to the right. If this number is greater than 25, then we mod it by 26 for an index.

Decryption takes in 2 inputs: text and key (integer). The program changes the text character by character. We find the character in the alphabet list and note its index. The function decrypts the text by changing the index key-value spots to the left. If this number is less than 0, then we add it to 26 (alphabet size) for an index

Brute Force Attack decrypts text for 1 to 25 keys. It loops the decryption function. 
The program will repeat itself until the Exit option is selected.

Future updates: 
Using ASCII values instead of dev defined alphabet
Error checking and test suite