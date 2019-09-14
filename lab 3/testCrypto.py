Create a file called testCrypto.py. In testCrypto.py, test (and output the results) of both encrypt and decrypt 3 times.

def substitutionEncrypt(plainText ,key):

alphabet = "abcdefghijklmnopqrstuvwxyz"

plainText = plainText.lower ()

cipherText = ""

for ch in plainText:

btciph = alphabet.find(ch)

cipherText = cipherText + key[btcipher]

return cipherText

testKey1 = "zyxwvutsrqponmlkjihgfedcba"

TestKey2 = "wxyzabcdefghijklmnopqrstuv"

TestKey2 = "abcdefghijklmnopqrstuvwxyz"

cipherText = substitutionEncrypt("i went to the store",testKey1)

print(cipherText)

r dvmg gl gsv hgliv

cipherText = substitutionEncrypt("i went to the store",testKey2)

print(cipherText)

m airx xs xli wxsvi

