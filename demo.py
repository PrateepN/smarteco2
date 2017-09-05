import logging

from flask import Flask
from flask_ask import Ask, statement, question
from flask import json

app = Flask(__name__)
@app.route('/webhook2', methods=['POST'])
ask = Ask(app, "/")
@ask.launch
def launch():
    return statement("Welcome to the requests demo")

speech="We are working on that"
	
@ask.intent("Premium_amount")
def hello():
    response = app.response_class(
        response=json.dumps(data),
        status=200,
		speech: speech,
        mimetype='application/json'
    )
    return response

	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')