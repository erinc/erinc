import os
from flask import Flask
from flask import render_template
from flask import redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products/')
def products():
    return render_template('products.html')

@app.route('/resume/')
def hello():
    return redirect("https://dl.dropboxusercontent.com/u/169206/Erinc-Resume.pdf", code=302)

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)    