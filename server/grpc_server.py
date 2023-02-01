import json
import grpc
from concurrent import futures

import gRPC.coffee_pb2 as coffee_pb2
import gRPC.coffee_pb2_grpc as coffee_pb2_grpc

from server_func.coffeeMaker import making_coffee

class CoffeeServicer(coffee_pb2_grpc.CoffeeServicer):
    def OrderCoffee(self, request, context):
        print("We got some coffee order")
        print("request: ", request)
        try:
            request_json = json.loads(request.requestJsonStr)
            response_json = making_coffee(request_json['coffee'], "gRPC")
            response = coffee_pb2.CoffeeResponse()
            response.responseJsonStr = json.dumps(response_json)
        except Exception as e:
            print(f"Exception {e}")
        return response
        
def grpc_init():
    server = grpc.server (futures.ThreadPoolExecutor(max_workers=10))
    coffee_pb2_grpc.add_CoffeeServicer_to_server(CoffeeServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server started. Listening on port 50051')
    server.wait_for_termination()
    
if __name__ == '__main__':
    grpc_init()