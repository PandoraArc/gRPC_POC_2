from flask import Flask, request
from server_func.coffeeMaker import making_coffee

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_world():
    args = request.args.to_dict()
    print(args.get('coffee'))
    return making_coffee(args.get('coffee'), "RestAPI")

if __name__ == '__main__':
    app.run(port=5050)