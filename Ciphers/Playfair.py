#!/usr/bin/env python
# coding: utf-8

# In[1]:


def prepare_text(text, for_encryption=True):
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))

    result = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if i + 1 < len(text):
            b = text[i + 1]
            if a == b:
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X'
            i += 1
        result += a + b
    return result


def generate_matrix(key):
    key = key.upper().replace('J', 'I')
    seen = set()
    matrix = []

    for char in key:
        if char.isalpha() and char not in seen:
            seen.add(char)
            matrix.append(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in seen:
            seen.add(char)
            matrix.append(char)

    # Convert to 5x5 matrix
    mat = [matrix[i:i + 5] for i in range(0, 25, 5)]
    return mat

def print_matrix(mat):
    print("\nPlayfair Matrix:")
    for row in mat:
        print(' '.join(row))
    print()

def find_position(matrix, letter):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == letter:
                return i, j
    return None


def playfair_encrypt(plaintext, key):
    matrix = generate_matrix(key)
    print_matrix(matrix)
    plaintext = prepare_text(plaintext)

    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]

    return ciphertext


def playfair_decrypt(ciphertext, key):
    matrix = generate_matrix(key)
    ciphertext = prepare_text(ciphertext, for_encryption=False)

    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i + 1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]

    return plaintext


# In[3]:


#key = "Senior Project"
#text = "One month left"
#if double letters, split them up with an x. message into mesxsage
#text is split into 2
#I/J are combined

#print("Key:",key)
#print("Original message:",text)
#encrypted = playfair_encrypt(text, key)
#print("Encrypted:", encrypted)

#decrypted = playfair_decrypt(encrypted, key)
#print("Decrypted:", decrypted)


# In[ ]:




