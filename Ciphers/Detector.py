#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import base64

# In[2]:


def detect_possible_ciphers(ciphertext, num_keys=0, num_matrices=0):
    cleaned_text = re.sub(r'[^A-Z]', '', ciphertext.upper())

    cipher_list = {
        "Caesar",
        "Vigenère",
        "Atbash",
        "Playfair",
        "Hill",
        "Affine",
        "Four-Square",
        "Base64"
    }

    possible = set()
    ruled_out = set()

    if is_base64(ciphertext):
        possible.add("Base64")
        ruled_out |= (cipher_list - {"Base64"})
        return sorted(possible), sorted(ruled_out)

    for cipher in cipher_list:
        if cipher == "Caesar":
            if num_keys == 1:
                possible.add("Caesar")
            else:
                ruled_out.add("Caesar")

        elif cipher == "Vigenère":
            if num_keys == 1:
                possible.add("Vigenère")
            else:
                ruled_out.add("Vigenère")

        elif cipher == "Atbash":
            if num_keys == 0 and num_matrices == 0:
                possible.add("Atbash")
            else:
                ruled_out.add("Atbash")

        elif cipher == "Playfair":
            if num_matrices == 1:
                possible.add("Playfair")
            else:
                ruled_out.add("Playfair")

        elif cipher == "Hill":
            if num_matrices == 1:
                possible.add("Hill")
            else:
                ruled_out.add("Hill")

        elif cipher == "Affine":
            if num_keys == 1:
                possible.add("Affine")
            else:
                ruled_out.add("Affine")

        elif cipher == "Four-Square":
            if num_matrices == 2:
                possible.add("Four-Square")
            else:
                ruled_out.add("Four-Square")

        elif cipher == "Base64":
            ruled_out.add("Base64")

    return sorted(possible), sorted(ruled_out)

def is_base64(text):
    try:
        base64.b64decode(text, validate=True)
        return True
    except Exception:
        return False


# In[3]:


ciphertext = "KHOOR ZRUOG"
possible, ruled_out = detect_possible_ciphers(ciphertext, num_keys=2, num_matrices=2)
print("Possible Ciphers:", possible)
print("Ruled Out Ciphers:", ruled_out)


# In[ ]:




