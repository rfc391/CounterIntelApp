
import grpc
from concurrent import futures
import time

# Import the generated classes
import service_pb2
import service_pb2_grpc

# Define the service class
class MyService(service_pb2_grpc.MyServiceServicer):
    def ProcessRequest(self, request, context):
        response = service_pb2.MyResponse()
        response.message = f"Received: {request.input_data}"
        return response

# gRPC Server setup
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("Server started on port 50051")
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == "__main__":
    serve()
