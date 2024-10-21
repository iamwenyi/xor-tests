text = input("Enter text: ")
key = input("Enter key: ")
n = len(text)

cipher = ""

for i in range(n):
  t = text[i]
  k = key[i%len(key)]
  x = ord(k) ^ ord(t)
  p = format(x,'02x')
  cipher += p
  print (t, k, x, p)

print(cipher)



 
