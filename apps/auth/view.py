from libs.protos.output.auth_pb2_grpc import AuthServicer
from libs.protos.output.auth_pb2 import UserInfo
from libs.db.mysql.connection import connection
from apps.auth.controller import AuthController

class Auth(AuthServicer):
    
    def Create(self, request, context):
        auth_controller = AuthController()
        conn = None
        
        try:
            conn = connection()
            response = auth_controller.create(conn, request)
            conn.commit()

            return UserInfo(user_id = response['id'],
                            email = response['email'],
                            nickname = response['nickname'],
                            created_at = response['created_at'],
                            is_deleted = response['is_deleted'])
            

        except Exception as e:
            conn.rollback()
            raise e
        
        finally:
            conn.close()