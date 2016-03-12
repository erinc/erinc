import os
import requests
import json

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request


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

@app.route('/zapier/')
def zapier():
    headers = {'content-type': 'application/json'}
    zapier_hook_url = 'https://zapier.com/hooks/catch/2ga883/'
    referer = request.referrer
    try:
        ip = request.access_route[0]
    except:
        ip = request.remote_addr
    data = {'referer':referer, 'ip':ip, 'page':'zapier'}
    requests.post(zapier_hook_url, data=json.dumps(data), headers=headers)

    return render_template('zapier.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)    