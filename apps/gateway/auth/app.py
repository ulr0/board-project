import os
import sys
import uvicorn
import pymysql

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from libs.db.mysql.connection import connection
import test_client

class User(BaseModel):
    email: str
    nickname: str
    password: str
    created_at: str
    is_deleted: bool

app = FastAPI()

@app.get('/')
def hiroo():
    
    return {'hi':'roo'}

@app.post('/test')
def test(user: User):
    # conn = connection()
    # query = """
    #     INSERT INTO users(
    #         email,
    #         nickname,
    #         password,
    #         created_at,
    #         is_deleted
    #     )
    #     VALUES(
    #         %(email)s,
    #         %(nickname)s,
    #         %(password)s,
    #         %(created_at)s,
    #         %(is_deleted)s
    #         )
    #     """

    # with conn.cursor(pymysql.cursors.DictCursor) as cursor:
    #     cursor.execute(query, dict(user))
    
    # conn.commit()
    
    result = test_client.run(user)
    
    return {'user_id' : result.user_id, 'email' : result.email, 'nickname' : result.nickname}

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)