from fastapi import APIRouter
from pydantic import BaseModel, Field

class NewUserInfo(BaseModel):
    email: str = Field(regex='^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    nickname: str = Field(regex='^[가-힣|a-z|A-Z|0-9]+$', min_length=2, max_length=12)
    password: str = Field(min_length=6, max_length=15)

router = APIRouter()

class Auth():
    
    @router.post('/signup')
    def signup(data: NewUserInfo):
        # 클라이언트로 연결..

        return data