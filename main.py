from flask import Flask

app = Flask('first')
@app.route('/')
def home():
    return('this is home')
@app.route('/second')
def biju():
    return('Welcome to the second page')

app.run()