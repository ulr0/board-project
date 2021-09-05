import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from concurrent import futures
import grpc

from libs.protos.output import test_pb2, test_pb2_grpc

class Test(test_pb2_grpc.TestServicer):

    def Add(self, request, context):
        
        return test_pb2.AddResponse(user_id=1, email=request.email, nickname=request.nickname)

def serve():
    print('Server start')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    test_pb2_grpc.add_TestServicer_to_server(Test(), server)

    server.add_insecure_port('[::]:50050')

    server.start()

    server.wait_for_termination()

if __name__ == '__main__':
    serve()
