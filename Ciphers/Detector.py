#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import base64
import numpy as np


# In[2]:


def detect_possible_ciphers(ciphertext, keys=None, matrices=None):
    keys = keys or []
    matrices = matrices or []

    # Normalize ciphertext
    cleaned_text = re.sub(r'[^A-Z]', '', ciphertext.upper())

    # Define all ciphers we are evaluating
    all_ciphers = {
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

    # --- Base64 Detection ---
    if is_base64(ciphertext):
        possible.add("Base64")
        ruled_out |= (all_ciphers - {"Base64"})
        return sorted(possible), sorted(ruled_out)

    # --- Cipher Rules ---

    for cipher in all_ciphers:
        if cipher == "Caesar":
            if not keys:
                ruled_out.add("Caesar")
            elif len(keys) == 1 and isinstance(keys[0], str) and len(keys[0]) == 1:
                possible.add("Caesar")
            else:
                ruled_out.add("Caesar")

        elif cipher == "Vigenère":
            if not keys:
                ruled_out.add("Vigenère")
            elif len(keys) == 1 and isinstance(keys[0], str) and len(keys[0]) > 1:
                possible.add("Vigenère")
            else:
                ruled_out.add("Vigenère")

        elif cipher == "Atbash":
            if keys or matrices:
                ruled_out.add("Atbash")
            else:
                possible.add("Atbash")

        elif cipher == "Playfair":
            if matrices and len(matrices) == 1:
                possible.add("Playfair")
            else:
                ruled_out.add("Playfair")

        elif cipher == "Hill":
            if matrices and len(matrices) == 1:
                possible.add("Hill")
            else:
                ruled_out.add("Hill")

        elif cipher == "Affine":
            if keys and isinstance(keys[0], tuple) and len(keys[0]) == 2:
                possible.add("Affine")
            else:
                ruled_out.add("Affine")

        elif cipher == "Four-Square":
            if matrices and len(matrices) == 2:
                possible.add("Four-Square")
            else:
                ruled_out.add("Four-Square")

        elif cipher == "Base64":
            ruled_out.add("Base64")  # already handled above

    return sorted(possible), sorted(ruled_out)

# --- Utilities ---

def is_base64(text):
    try:
        base64.b64decode(text, validate=True)
        return True
    except Exception:
        return False


# In[5]:


# --- Example Usage ---

ct1 = "KHOOR ZRUOG"
keys1 = []
matrices1 = ["D"]

possible, ruled_out = detect_possible_ciphers(ct1, keys1, matrices1)
print("Possible Ciphers:", possible)
print("Ruled Out Ciphers:", ruled_out)


# In[ ]:




