from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tariffe')
def tariffe():
    return render_template('tariffe.html')

@app.route('/contattaci')
def contattaci():
    return render_template('contattaci.html')

if __name__ == '__main__':
    app.run(debug=True)