cipher = input("Enter cipher: ")
key = input("Enter key: ")

text = ""

for i in range(0, len(cipher), 2):
    p = cipher[i:i+2]           # Get the two-character hexadecimal string
    x = int(p, 16)              # Convert the hex string back to an integer
    k = key[(i//2) % len(key)]  # Get the corresponding character from the key
    t = chr(x ^ ord(k))         # XOR with the key character and convert back to a character
    text += t                   # Append the character to the text
    print (p, x, k, t)

print(text)