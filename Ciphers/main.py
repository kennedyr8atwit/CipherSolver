from flask import Flask, render_template, request
from Caesar import crack_caesar
from ATBash import atbash
from Vigenere import vigenere_encrypt, vigenere_decrypt
from Playfair import playfair_encrypt, playfair_decrypt


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    caesar_result = None
    atbash_result = None
    vigenere_result = None
    playfair_result = None

    if request.method == 'POST':
        action = request.form.get('action')
        ciphertext = request.form.get('ciphertext', '').strip()
        key = request.form.get('key', '').strip()

        if action == 'caesar':
            shift, decrypted_text = crack_caesar(ciphertext)
            caesar_result = f"<b>Caesar Cipher</b><br>Best Shift: {shift}<br>Decrypted Text: {decrypted_text}"
            
        elif action == 'atbash':
            decrypted_text = atbash(ciphertext)
            atbash_result = f"<b>Atbash Cipher</b><br>Decrypted Text: {decrypted_text}"
            
        elif action == 'vigenere_decrypt':
            if key:
                decrypted_text = vigenere_decrypt(ciphertext, key)
                vigenere_result = f"<b>Vigenère Cipher</b><br>Key: {key}<br>Decrypted Text: {decrypted_text}"
            else:
                vigenere_result = "<b>Error:</b> Key is required for Vigenère decryption."

        elif action == 'vigenere_encrypt':
            if key:
                encrypted_text = vigenere_encrypt(ciphertext, key)
                vigenere_result = f"<b>Vigenère Cipher</b><br>Key: {key}<br>Encrypted Text: {encrypted_text}"
            else:
                vigenere_result = "<b>Error:</b> Key is required for Vigenère encryption."
                
        elif action == 'playfair_decrypt':
            if key:
                decrypted_text = playfair_decrypt(ciphertext, key)
                playfair_result = f"<b>Playfair Cipher</b><br>Key: {key}<br>Decrypted Text: {decrypted_text}"
            else:
                playfair_result = "<b>Error:</b> Key is required for Playfair decryption."

        elif action == 'playfair_encrypt':
            if key:
                encrypted_text = playfair_encrypt(ciphertext, key)
                playfair_result = f"<b>Playfair Cipher</b><br>Key: {key}<br>Encrypted Text: {encrypted_text}"
            else:
                playfair_result = "<b>Error:</b> Key is required for Playfair encryption."


    return render_template('index.html', 
        caesar_result=caesar_result,
        atbash_result=atbash_result,
        vigenere_result=vigenere_result,
        playfair_result=playfair_result
    )

if __name__ == '__main__':
    app.run(debug=True)
