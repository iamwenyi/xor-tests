import string

binarytext = input("Enter ciphertext (in binary): ")
key = input("Enter key: ")

n = len(binarytext)

cleartext = ""
chars = []

for i in range(0, n, 8):
    byte = binarytext[i:i+8]
    ascii_value = int(byte, 2)
    chars.append(ascii_value)
    
for i in range(len(chars)):
    t = chars[i]
    k = ord(key[i%len(key)])
    x = t ^ k
    cleartext += chr(x)

print("Decrypted message: " + cleartext)