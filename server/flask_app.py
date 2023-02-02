from flask import Flask, request
import time

import threading

import grpc
from concurrent import futures

from server_func.coffeeMaker import making_coffee
from server_func.resopnsePing import pingPongJson

import gRPC.coffee_pb2 as coffee_pb2
import gRPC.coffee_pb2_grpc as coffee_pb2_grpc

app = Flask(__name__)

class CoffeeServicer(coffee_pb2_grpc.CoffeeServicer):
    def OrderCoffee(self, request, context):
        print("We got some coffee order")
        print("request: ", request)
        try:
            # request_json = json.loads(request.requestJsonStr)
            # response_json = making_coffee(request_json['coffee'], "gRPC")
            response = coffee_pb2.CoffeeResponse()
            # response.responseJsonStr = json.dumps(response_json)
            response.responseJsonStr = pingPongJson(request.requestJsonStr)
        except Exception as e:
            print(f"Exception {e}")
        return response

def grpc_init():
    server = grpc.server (futures.ThreadPoolExecutor(max_workers=10))
    coffee_pb2_grpc.add_CoffeeServicer_to_server(CoffeeServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started. Listening on port 50051')
    while True:
        print("server is now running")
        time.sleep(30)
        

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
    t = threading.Thread(target=grpc_init)
    t.start()
    app.run(port=5050)