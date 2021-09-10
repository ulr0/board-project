import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

import grpc
from concurrent import futures

from libs.protos.output.auth_pb2_grpc import add_AuthServicer_to_server
from apps.auth.view import Auth

def serve():
    print('Server start')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_AuthServicer_to_server(Auth(), server)

    server.add_insecure_port('[::]:50050')

    server.start()

    server.wait_for_termination()

if __name__ == '__main__':
    serve()