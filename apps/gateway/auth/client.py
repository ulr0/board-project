import grpc

from libs.protos.output.auth_pb2 import SignupRequest
from libs.protos.output.auth_pb2_grpc import AuthStub

class Auth:
    def create(data):
        channel = grpc.insecure_channel('localhost:50050')
        stub = AuthStub(channel)
        
        response = stub.Create(SignupRequest(email = data.email, 
                                        nickname = data.nickname,
                                        password = data.password))
    
        return response