import string
import nltk
from nltk.corpus import words

# Make sure words corpus is downloaded before running this script
# nltk.download('words')  # Uncomment if running first time

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

    return best_shift, best_decryption





