from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/test')
def testing_the_world():
    return jsonify(test_data='hello',
                   test='ttttt', terer="wsdfsdf")

app.run()
