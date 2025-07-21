from flask import Flask, render_template, request
from Caesar import crack_caesar
from ATBash import atbash
from Vigenere import vigenere_encrypt, vigenere_decrypt
from Playfair import playfair_encrypt, playfair_decrypt, generate_matrix
from FourSquare import four_square_encrypt, four_square_decrypt, show_four_squares_2x2
from Detector import detect_possible_ciphers


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    caesar_result = None
    atbash_result = None
    vigenere_result = None
    playfair_result = None
    foursquare_result = None
    detection_result = None

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
                matrix = generate_matrix(key)
                playfair_result = f"<b>Playfair Cipher</b><br>Key: {key}<br>Encrypted Text: {encrypted_text}"
            else:
                playfair_result = "<b>Error:</b> Key is required for Playfair encryption."
                matrix = None

        elif action == 'foursquare_encrypt':
            plaintext = request.form.get('plaintext', '').strip()
            key1 = request.form.get('key1', '').strip()
            key2 = request.form.get('key2', '').strip()
            if plaintext and key1 and key2:
                encrypted_text = four_square_encrypt(plaintext, key1, key2)
                foursquare_result = f"<b>Encrypted with FourSquare</b><br>Keys: {key1}, {key2}<br>Ciphertext: {encrypted_text}"
            else:
                foursquare_result = "<b>Error:</b> Plaintext and both keys are required."

        elif action == 'foursquare_decrypt':
            ciphertext = request.form.get('ciphertext', '').strip()
            key1 = request.form.get('key1', '').strip()
            key2 = request.form.get('key2', '').strip()
            if ciphertext and key1 and key2:
                decrypted_text = four_square_decrypt(ciphertext, key1, key2)
                foursquare_result = f"<b>Decrypted with FourSquare</b><br>Keys: {key1}, {key2}<br>Plaintext: {decrypted_text}"
            else:
                foursquare_result = "<b>Error:</b> Ciphertext and both keys are required."

        elif action == 'show_foursquare':
            key1 = request.form.get('key1', '').strip()
            key2 = request.form.get('key2', '').strip()
            if key1 and key2:
                import io, contextlib
                buf = io.StringIO()
                with contextlib.redirect_stdout(buf):
                    show_four_squares_2x2(key1, key2)
                output = buf.getvalue().replace('\n', '<br>')
                foursquare_result = f"<b>FourSquare Cipher Grids:</b><br>{output}"
            else:
                foursquare_result = "<b>Error:</b> Both keys are required to display the squares."
        
        elif action == 'detect_ciphers':
            ciphertext = request.form.get('ciphertext', '').strip()
            num_keys = int(request.form.get('num_keys', 0))
            num_matrices = int(request.form.get('num_matrices', 0))
            
            possible, ruled_out = detect_possible_ciphers(ciphertext, num_keys, num_matrices)
            
            detection_result = {
                "possible": possible,
                "ruled_out": ruled_out
            }



    return render_template('index.html', 
        caesar_result=caesar_result,
        atbash_result=atbash_result,
        vigenere_result=vigenere_result,
        playfair_result=playfair_result,
        playfair_matrix=matrix if 'matrix' in locals() else None,
        foursquare_result=foursquare_result,
        detection_result=detection_result if 'detection_result' in locals() else None
    )

if __name__ == '__main__':
    app.run(debug=True)
