from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world. Next add /test to the URL.'

@app.route('/test')
def test_page():
    return "This is your test page"
