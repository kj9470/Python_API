# 플라스크 연습
from flask import Flask
app = Flask(__name__)

@app.route('/') #서버를 구축한다

def index():
    return '<h1> Hello World </h1>'

if __name__ == "__main__":
    app.run(debug=True, port=5000)
