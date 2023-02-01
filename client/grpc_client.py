import grpc
import json
import gRPC.coffee_pb2 as coffee_pb2
import gRPC.coffee_pb2_grpc as coffee_pb2_grpc

request = "{\"coffee\": \"latte\"}"

def run(order):
    request = {
        "coffee": order
    }
    request = json.dumps(request)
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = coffee_pb2_grpc.CoffeeStub(channel)
        request = coffee_pb2.CoffeeRequest(requestJsonStr=request)
        print("calling server")
        response = stub.OrderCoffee(request)
        print("get response")
        print(json.loads(response.responseJsonStr))

if __name__ == "__main__":
    print("type input ? ")
    order = str(input())
    run(order)
        
    