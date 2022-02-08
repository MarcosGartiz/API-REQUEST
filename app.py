from flask import Flask, render_template
import requests
import json

app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    req = requests.get('https://api.ipdata.co/?api-key=6ab11adc837e48e0d56a9a1f171c604497134baf2c6bad95b93ad5ab')
    data=json.loads(req.content)
    return render_template('index.html', data=data)
   