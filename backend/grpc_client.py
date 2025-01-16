
import grpc
import service_pb2
import service_pb2_grpc

# gRPC Client setup
def call_grpc_service(input_data):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = service_pb2_grpc.MyServiceStub(channel)
        request = service_pb2.MyRequest(input_data=input_data)
        response = stub.ProcessRequest(request)
    return response.message

# Example usage
if __name__ == "__main__":
    result = call_grpc_service("Test Input")
    print("Response from gRPC Server:", result)
