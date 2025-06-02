from flask import Flask, render_template, request
from caesar import crack_caesar  # import your function

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        ciphertext = request.form.get('ciphertext', '')
        shift, decrypted_text = crack_caesar(ciphertext)
        result = f"Best shift: {shift} <br>Decrypted Text: {decrypted_text}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)