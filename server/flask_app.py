from flask import Flask, request
from server_func.coffeeMaker import making_coffee
from server_func.resopnsePing import pingPongJson

app = Flask(__name__)

@app.route("/", methods=['POST'])
def hello_world():
    args = request.args.to_dict()
    # print(args.get('coffee'))
    # return making_coffee(args.get('coffee'), "RestAPI")
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return pingPongJson(json)
    else:
        return 'Content-Type not supported!'

if __name__ == '__main__':
    app.run(port=5050)