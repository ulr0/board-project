import os
import sys
import uvicorn
import pymysql

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))

from fastapi import FastAPI
from pydantic import BaseModel

from libs.db.mysql.connection import connection

class User(BaseModel):
    email: str
    nickname: str
    password: str
    created_at: str
    is_deleted: bool

app = FastAPI()

@app.get('/')
def hiroo():
    print(__file__)
    return {'hi':'roo'}

@app.post('/test')
def test(user: User):
    conn = connection()
    query = """
        INSERT INTO users(
            email,
            nickname,
            password,
            created_at,
            is_deleted
        )
        VALUES(
            %(email)s,
            %(nickname)s,
            %(password)s,
            %(created_at)s,
            %(is_deleted)s
            )
        """

    with conn.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute(query, dict(user))
    
    conn.commit()
    
    return user

if __name__ == '__main__':
    uvicorn.run('app:app', host='127.0.0.1', port=8000, reload=True)