from __future__ import print_function
#from future.standard_library import install_aliases
#install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps)

    res = processRequest(req)

    res = json.dumps
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

@ask.launch
def launch():
    return statement("Welcome to the requests demo")


@ask.intent("Premium_Intent")
def hello():
    return question("Who do you want me to say hello to?")


@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("Stopping")
	

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')