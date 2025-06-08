#!/usr/bin/env python
# coding: utf-8

# In[1]:


def vigenere_encrypt(plaintext, key):
    result = []
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            encrypted = chr((ord(char) - base + shift) % 26 + base)
            result.append(encrypted)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            base = ord('A') if char.isupper() else ord('a')
            decrypted = chr((ord(char) - base - shift) % 26 + base)
            result.append(decrypted)
            key_index += 1
        else:
            result.append(char)

    return ''.join(result)


# In[4]:


plaintext = "HELLO WORLD"
key = "SENIORPROJECT"
encrypted = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(encrypted, key)

print("Encrypted:", encrypted)
print("Decrypted:", decrypted)


# In[ ]:




