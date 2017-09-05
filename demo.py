import logging

from flask import Flask
from flask_ask import Ask, statement, question


app = Flask(__name__)
@app.route('/webhook2', methods=['POST'])
ask = Ask(app, "/")
@ask.launch
def launch():
    return statement("Welcome to the requests demo")


@ask.intent("Premium_amount")
def hello():
    return question("Who do you want me to say hello to?")



	
	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')