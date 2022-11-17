from flask import Flask, request

app = Flask(__name__)


database = {'wreet': '100', 'mridul':'141'}

@app.route('/home', methods= ['GET'])
def home():
    return "Welcome to my web API"

@app.route('/getdata', methods=['GET'])
def get_data():
    return database

@app.route('/adddata', methods=[ 'PUT'])
def add_data():
    key, value = list(request.args.items())[0]
    database[key] = value
    return f"{key} added"

@app.route('/deletedata', methods=['DELETE'])
def delete_data():
    key, value = list(request.args.items())[0]
    database.pop(value)
    return f"{value} deleted"

if __name__ == '__main__':
    app.run()