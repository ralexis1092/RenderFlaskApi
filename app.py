from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! This is a test!'


@app.route('/parameters', methods=['GET'])
def query_strings():

    args1 = request.args['a']
    args2 = request.args['b']
    args3 = request.args['c']

    return '''<h1>The Query String are...{}:{}:{}</h1>''' .format(args1,args2,args3)


@app.route('/add', methods=['GET'])
def add():

    args1 = request.args['a']
    args2 = request.args['b']

    return '''<h1>The Sum is {}</h1>''' .format(sum(args1,args2))