from flask import Flask, request
import json

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

    return '''<h1>The Sum is {}</h1>''' .format(int(args1) + int(args2)) if args1.isnumeric() and args2.isnumeric() else '''<h1>The Combined String is {}</h1>''' .format(args1 + args2)


@app.route('/reset')
def reset():
    # as requested in comment
    d = {}
    d["Alexis"] = 10
    d["Omar"] = 15
    try:
        with open("database.json", "w") as outfile: 
            json.dump(d, outfile)
    except:
         return '''<h1>Database couldnt be reset<h1>'''
    return '''<h1>Database has reset<h1>'''

@app.route('/remove')
def remove():
    # as requested in comment
    d = {}
    try:
        with open("database.json", "w") as outfile: 
            json.dump(d, outfile)
    except:
         return '''<h1>Database couldnt be removed<h1>'''
    return '''<h1>Database has removed<h1>'''

@app.route('/increment')
def increment():
    
    data = {}
    
 
    # Opening JSON file
    try:
        with open('database.json', "r") as json_file:
            data = json.load(json_file)
            for key in data:
                data["key"] += 5
            # for reading nested data [0] represents
            # the index value of the list

        with open('database.json', "w") as json_file:
            json.dump(data, json_file)
    except:
        return '''<h1>Couldn't increment<h1>'''

    return '''<h1>Database has incremented<h1>'''

@app.route('/view')
def view():
    
    data = {}

    try:
        # Opening JSON file
        with open('database.json', "r") as json_file:
            data = json.load(json_file)
    except:
        return '''<h1>Database is empty<h1>'''
    
    count = 0 
    s = "<h1>"
    for key in data:
        print(key)
        s += str(key) + ": " + str(data[key])
        
        count += 1
        if count < len(data):
            s += "<br />"

    s += "<h1>"    
    return s if data else '''<h1>Database is empty<h1>'''