
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI(title='基本 HTTP 认证示例')

# 创建 HTTPBasic 实例，用于处理认证
security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = "admin"
    correct_password = "password123"  # 实际应用中应使用安全的方式存储密码
    if credentials.username!= correct_username or credentials.password!= correct_password:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return credentials.username

@app.get("/secure_data/")
async def get_secure_data(username: str = Depends(get_current_username)):
    return {"data": "This is secure data only accessible to authenticated users."}
if __name__ == '__main__':
    uvicorn.run(app)