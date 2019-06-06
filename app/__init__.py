from flask import Flask
from flask import jsonify
from flask_pymongo import PyMongo


app = Flask(__name__)

app.config.from_object('config')

mongo = PyMongo(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/test')
def testing_the_world():
    return jsonify(test_data='hello',
                   test='ttttt', terer="wsdfsdf")


@app.route('/test/')
def test_function():
    return 'this is dummy test function'


@app.route('/testing/')
def testing_function():
    return 'this is dummy testing function'


@app.route('/variables/<test_variable>')
def show_variable(test_variable):
    return 'the test variable is %s' % test_variable


@app.route('/testdata')
def mongo_users():
    data = mongo.db.testCollection.find({})
    for value in data:
        print(value)
    return 'the dummy data is  %s' % value


