#!/usr/bin/env python
# coding: utf-8

# In[5]:


def atbash(text):
    result = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                #A-Z to Z-A
                result.append(chr(65 + (25 - (ord(char) - 65))))
            else:
                #a-z to z-a
                result.append(chr(97 + (25 - (ord(char) - 97))))
        else:
            result.append(char)
    return ''.join(result)


# In[9]:


text = "Svool, Dliow!"
decrpted_text = atbash(text)
print("Decrypted text:", cipher_text)
print("Decrypted back:", atbash(cipher_text))


# In[ ]:




