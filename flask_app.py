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
    headers = {'content-type': 'application/json'}
    zapier_hook_url = 'https://zapier.com/hooks/catch/2q9we8/'
    referer = request.referrer
    try:
        ip = request.access_route[0]
    except:
        ip = request.remote_addr
    data = {'referer':referer, 'ip':ip, 'page':'products'}
    try:
        requests.post(zapier_hook_url, data=json.dumps(data), headers=headers)
    except:
        pass    

    return render_template('products.html')

@app.route('/resume/')
def resume():
    headers = {'content-type': 'application/json'}
    zapier_hook_url = 'https://zapier.com/hooks/catch/2q9we8/'
    referer = request.referrer
    try:
        ip = request.access_route[0]
    except:
        ip = request.remote_addr
    data = {'referer':referer, 'ip':ip, 'page':'resume'}
    try:
        requests.post(zapier_hook_url, data=json.dumps(data), headers=headers)
    except:
        pass         
    return redirect("https://dl.dropboxusercontent.com/u/169206/Erinc_resume.pdf", code=302)


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
    try:
        requests.post(zapier_hook_url, data=json.dumps(data), headers=headers)
    except:
        pass

    return render_template('zapier.html')


@app.route('/magpie/')
def magpie():
    return render_template('magpie.html')


@app.route('/2025/')
def wealthfront():
    headers = {'content-type': 'application/json'}
    zapier_hook_url = 'https://zapier.com/hooks/catch/2q9we8/'
    referer = request.referrer
    try:
        ip = request.access_route[0]
    except:
        ip = request.remote_addr
    data = {'referer':referer, 'ip':ip, 'page':'wealthfront'}
    try:
        requests.post(zapier_hook_url, data=json.dumps(data), headers=headers)
    except:
        pass       
    return render_template('wealthfront.html')    


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)    