from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext



SECRET_KEY= "supersecretkey" # becomes env variable
ALGORITHM= "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") #print working directory

#Method to hash password
def hash_password(password: str):
    return pwd_context.hash(password)

#Method to verify given password
def verify_password(plain_password, hashed):
    return pwd_context.verify(plain_password, hashed)


#Method to create JWT token

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)