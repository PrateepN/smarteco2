import logging

from flask import Flask
from flask_ask import Ask, statement, question


app = Flask(__name__)
ask = Ask(app, "/webhook2")
log = logging.getLogger()
log.addHandler(logging.StreamHandler())
log.setLevel(logging.DEBUG)
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def launch():
    return statement("Welcome to the requests demo")


@ask.intent("Premium_amount")
def hello():
    return question("Who do you want me to say hello to?")


@ask.intent("AMAZON.StopIntent")
def stop():
    return statement("Stopping")
	
	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')