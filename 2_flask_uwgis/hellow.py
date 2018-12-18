from flask import Flask

app=Flask(__name__)

@app.route('/')

def index():
    return '<h1> HELLOW </h1>'

if __name__=='__main__':
     app.run('127.0.0.1')
