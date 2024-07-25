import uvicorn
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI(title='基本 HTTP 认证示例')

# 创建 HTTPBasic 实例，用于处理认证
security = HTTPBasic()

@app.get('/login')
async def login(credentials: HTTPBasicCredentials = Depends(security)):
    # 检查用户名和密码是否正确
    if credentials.username!= 'your_username' or credentials.password!= 'your_password':
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail='用户名或密码错误',
            headers={'WWW-Authenticate': 'Basic'}
        )
    else:
        return PlainTextResponse('登录成功')
if __name__ == '__main__':
    uvicorn.run(app)