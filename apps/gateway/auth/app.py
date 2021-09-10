import os, sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))

import uvicorn
from fastapi import FastAPI

from apps.gateway.auth.view import router

app = FastAPI()
app.include_router(router)

# @app.post('/signup')
# def signup(data: NewUserInfo):
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
    
    # result = test_client.run(user)
    
    # return {'user_id' : result.user_id, 'email' : result.email, 'nickname' : result.nickname}
    # return data

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)