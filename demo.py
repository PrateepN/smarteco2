import logging

from flask import Flask
from flask_ask import Ask, statement, question
from flask import jsonify

app = Flask(__name__)
@app.route('/webhook2', methods=['POST'])
ask = Ask(app, "/")
@ask.launch
def launch():
    return statement("Welcome to the requests demo")

response="We are working on that"
	
@ask.intent("Premium_amount")
def hello():
    return jsonify(response)



	
	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')