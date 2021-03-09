import json
from requests import post
from flask import Flask, render_template, request

app = Flask(__name__)

pub_key = None
response = {}

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        success()
    return render_template('home.html', pub_key=pub_key)


@app.route('/success', methods=['GET', 'POST'])
def success():
    captcha_response = request.form['g-recaptcha-response']
    print(captcha_response)
    response['g-recaptcha-response'] = captcha_response
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run()
