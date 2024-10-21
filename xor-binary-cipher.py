cleartext = input("Enter text: ")
key = input("Enter key: ")
n = len(cleartext)

ciphertext = ""

for i in range(n):
    t = cleartext[i]
    k = key[i%len(key)]
    x = ord(k) ^ ord(t)
    p = format(x,'08b')
    ciphertext += p
    print (t, k, x, p)

print(ciphertext)



 
