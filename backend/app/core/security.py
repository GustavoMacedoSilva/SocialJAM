from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

def HashPWD(password:str):
    hashed_pwd = pwd_cxt.hash(password)
    return hashed_pwd