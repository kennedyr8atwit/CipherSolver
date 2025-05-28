#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#caesar cipher logic


# In[15]:


get_ipython().system('pip install nltk')


# In[18]:


import sys
print(sys.executable)


# In[10]:


import nltk
import string
from nltk.corpus import words

# Load the set of English words
english_words = set(words.words())

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        else:
            decrypted += char
    return decrypted

def is_valid_word(word):
    # Remove punctuation, convert to lowercase
    word = word.strip(string.punctuation).lower()
    return word in english_words

def crack_caesar(ciphertext):
    max_valid_words = 0
    best_shift = 0
    best_decryption = ""

    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        words_list = decrypted.split()
        valid_count = sum(1 for word in words_list if is_valid_word(word))

        if valid_count > max_valid_words:
            max_valid_words = valid_count
            best_shift = shift
            best_decryption = decrypted
    print("Shift:", best_shift)
    print("Decrypted text:", best_decryption)


# In[12]:


# Example usage
ciphertext = "Zlupvy wyvqlja slaz nv"
crack_caesar(ciphertext)


# In[ ]:




