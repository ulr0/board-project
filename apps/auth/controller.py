import bcrypt
from google.protobuf.json_format import MessageToDict

from apps.auth.model import AuthModel

class AuthController:
    def create(self, connection, data):
        auth_model = AuthModel()
        try:
            data = MessageToDict(data)
            
            hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            data['password'] = hashed_password
            
            user_id = auth_model.create(connection, data)
            user_info = auth_model.get_user_info(connection, user_id)
            user_info['created_at'] = str(user_info['created_at'])
            user_info['is_deleted'] = str(user_info['is_deleted'])
            
            return user_info

        except Exception as e:
            raise e