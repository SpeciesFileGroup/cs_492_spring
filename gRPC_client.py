import random
import time
import sys
import os
import grpc
import my_service_pb2 as my_service_pb2
import my_service_pb2_grpc as my_service_pb2_grpc
import math
from visualization import Visualization


#integration with GRPC
class gRPCClient():
    def __init__(self):
        channel = grpc.insecure_channel('localhost:50051')
        self.stub = my_service_pb2_grpc.MyServiceStub(channel)

    def method1(self, filename, count):
        print('method 1')
        return self.stub.MyMethod1(my_service_pb2.MyRequest(filename=filename, count=count))

    def method2(self, number_of_pages):
        print('Counting number of pages...')
        return self.stub.MyMethod2(my_service_pb2.InitialRequest(number_of_pages=number_of_pages))

    def method3(self, req):
        print('method 3')
        return self.stub.MyMethod3(req)

    def query_stream(self, req):
        print('Streaming response back...')
        return self.stub.MyMethod4(req)

def queryPages(page_count, number_of_pages):  
    reqs = []
    for i in range(int(page_count/number_of_pages)):
        reqs.append(my_service_pb2.QueryRequest(offset=i*number_of_pages))

    for req in reqs:
        yield req

def main():
    number_of_pages = 10000
    if len(sys.argv[1:]):
        number_of_pages = int(sys.argv[1])

    client = gRPCClient()
    page_count = client.method2(number_of_pages).count
    res = client.query_stream(queryPages(page_count, number_of_pages))

    count = 0
    for re in res:
        viz = Visualization(tile_number = count, tile_width = 100, tile_height = 100, data_list = list(zip(re.page_names, re.page_count)))
        viz.visualize_data()
        count += 1

if __name__ == '__main__':
    main()