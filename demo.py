import logging

from flask import Flask
from flask_ask import Ask, statement, question
from flask import jsonify

app = Flask(__name__)
@app.route('/webhook2', methods=['POST'])
ask = Ask(app, "/")
@ask.launch
def launch():
    return statement(jsonify({'speech':"Welcome to the requests demo"}))

speech="We are working on that"
	


	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')