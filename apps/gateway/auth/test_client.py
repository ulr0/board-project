import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

import grpc

from libs.protos.output.test_pb2 import AddRequest
from libs.protos.output.test_pb2_grpc import TestStub

def run(user):
    
    channel = grpc.insecure_channel('localhost:50050')
    stub = TestStub(channel)
    
    response = stub.Add(AddRequest(email=user.email, nickname=user.nickname, password=user.password, created_at=user.created_at, is_deleted=user.is_deleted))
    
    return response
if __name__ == '__main__':
    run()