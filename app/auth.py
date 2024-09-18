from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

# Пользователи
USERS = {
    "user1": "password1",
    "user2": "password2",
}

security = HTTPBasic()


# Функция аутентификации
def authenticate(credentials: HTTPBasicCredentials = Depends(security)) -> str:
    username = credentials.username
    password = credentials.password
    if username in USERS and USERS[username] == password:
        return username
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Basic"},
    )
