from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        # Grab data from form input
        name = request.form.get('name', 'Stranger')
        # Run some Python logic
        message = f"Hello, {name}! This message is from Python."
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)