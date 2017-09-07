import logging

from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify


from flask_ask import Ask, statement, question


app = Flask(__name__)
@app.route('/webhook2', methods=['POST'])

def login():
		if request.method == 'POST':
        test = request.data
        return test

	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')