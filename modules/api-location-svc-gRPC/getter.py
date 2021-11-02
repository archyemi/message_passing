import grpc
import location_pb2
import location_pb2_grpc


print("Getting sample payload...")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

location_id = location_pb2.LocationID(id=1)

response = stub.Get(location_id)
print(response)