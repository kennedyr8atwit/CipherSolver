#!/usr/bin/env python
# coding: utf-8

# In[1]:


import string


# In[2]:


def generate_square(key):
    key = key.upper().replace('Q', '').replace('J', 'I')
    seen = set()
    square = []
    
    #skipped if  no key
    for char in key + string.ascii_uppercase:
        if char in seen or char == 'Q':
            continue
        seen.add(char)
        square.append(char)
    return [square[i:i+5] for i in range(0, 25, 5)]

def format_row(row1, row2):
    return ' '.join(row1) + '    ' + ' '.join(row2)

def show_four_squares_2x2(key1="", key2=""):
    TL = generate_square("")
    TR = generate_square(key1)
    BL = generate_square(key2)
    BR = generate_square("")

    print("\nFourSquare Cipher Grids:\n")
    print("TL           TR (Key)")
    for row1, row2 in zip(TL, TR):
        print(format_row(row1, row2))
    print()
    print("BL (Key)     BR")
    for row1, row2 in zip(BL, BR):
        print(format_row(row1, row2))
    print()

def preprocess_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(c for c in text if c in string.ascii_uppercase)
    # pad if odd length
    if len(text) % 2 != 0:
        text += 'X'  
    return text

def find_position(letter, square):
    for row_idx, row in enumerate(square):
        if letter in row:
            return (row_idx, row.index(letter))
    raise ValueError(f"Letter {letter} not found in square")

def encrypt_digraph(digraph, TL, TR, BL, BR):
    a, b = digraph
    row_a, col_a = find_position(a, TL)
    row_b, col_b = find_position(b, BR)
    return TR[row_a][col_b] + BL[row_b][col_a]

def decrypt_digraph(digraph, TL, TR, BL, BR):
    a, b = digraph
    row_a, col_a = find_position(a, TR)
    row_b, col_b = find_position(b, BL)
    return TL[row_a][col_b] + BR[row_b][col_a]

def four_square_encrypt(text, key1, key2):
    TL = generate_square("") 
    TR = generate_square(key1)
    BL = generate_square(key2)
    BR = generate_square("")

    text = preprocess_text(text)
    return ''.join(encrypt_digraph(text[i:i+2], TL, TR, BL, BR) for i in range(0, len(text), 2))

def four_square_decrypt(ciphertext, key1, key2):
    TL = generate_square("")
    TR = generate_square(key1)
    BL = generate_square(key2)
    BR = generate_square("")

    return ''.join(decrypt_digraph(ciphertext[i:i+2], TL, TR, BL, BR) for i in range(0, len(ciphertext), 2))


# In[4]:


# === Example usage ===
#key1 = "example"
#key2 = "potato"
#show_four_squares_2x2(key1, key2)

#plaintext = "senior project"
#cipher = four_square_encrypt(plaintext, key1, key2)
#decrypted = four_square_decrypt(cipher, key1, key2)

#print("Encrypted:", cipher)
#print("Decrypted:", decrypted)


# In[ ]:





# In[ ]:




