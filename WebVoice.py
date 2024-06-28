from aip import AipSpeech
from flask import Flask, request, render_template, send_from_directory
import datetime
import os

APP_ID = 'XXX'
API_KEY = 'XXX'
SECRET_KEY = 'XXX'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

preS = '''
<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <title>login</title>
  </head>
  <body>
    <form method="post" action="/result">
        <span >请输入文字</span><br/>
        <input type="text" style="width: 100%; height: 100px;" name="username" id="username">
        <br/>
        <button type="submit" style="width: 100%; height: 40px" id="loginBtn">播放</button>
    </form>
    <audio controls>
        <source src="
'''
rearS = '''
" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
  </body>
</html>
'''

app = Flask(__name__)
class UserInfo:
    def __init__(self):
        self.id = 'default'


@app.route('/', methods=['GET','POST'])
def start():
    us.id = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return render_template('index.html')

@app.route('/result', methods=['GET','POST'])
def WebServer():
    us.id = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    result = client.synthesis(request.form.get('username'), 'zh', 1, {
        "format": "mp3-16k",
        "voice": 3,
        "lang": "zh",
        "speed": 5,
        "enable_subtitle": 2,
        "break": 200
    })
    if not isinstance(result, dict):
        with open('created/' + us.id + '.mp3', 'wb') as f:
            f.write(result)
    else:
        print(result)
    return preS + 'music/' + us.id + '.mp3' + rearS

@app.route('/music/<filename>', methods=['GET','POST'])
def download(filename):
    print(os.getcwd())
    return send_from_directory('created/', filename, as_attachment=True)

us = UserInfo()
app.run(host='0.0.0.0', port=52100)
