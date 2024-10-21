import string
import streamlit as st
#import nltk

#nltk.download('words')
#dictionary_words = set(nltk.corpus.words.words())     Streamlit doesn't support ntlk, will change soon

ascii_chars = [
    ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',',
    '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`',
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '{', '|', '}', '~'
]

def decipher(cipher, key):
    chars = []
    cleartext = ""
    for i in range(0, len(cipher), 8):
        byte = cipher[i:i+8]           
        ascii_value = int(byte, 2)
        chars.append(ascii_value)
        
    for i in range(len(chars)):
        t = chars[i]
        k = ord(key[i%len(key)])
        x = t ^ k        
        cleartext += chr(x)                   
    
    return (key, cleartext)

def keygen(i, j):
    char1 = ascii_chars[i]
    char2 = ascii_chars[j]   
    key = char1 + char2

    return key

def main():
    st.title("XOR Bruteforce-r")

    desc = st.write("Hello! Enter a ciphertext in binary and I'll try to bruteforce it using two-character keys from ASCII.")
    cipher = st.text_input("Enter ciphertext (in binary): ")

    if st.button("Bruteforce"):
        for i in range(0, len(ascii_chars)):
            for j in range(0, len(ascii_chars)):
                key = keygen(i,j)
                result = decipher(cipher, key)
                if result[1] in dictionary_words: #Error line
                    st.wrtie(f"The plaintext is", result[1], "and the key is", result[0])

main()
