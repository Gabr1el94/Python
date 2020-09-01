class Config:
    SECRET_KEY = b'\xc16\x80\x1c\xc9G\xe6hC\x84\xc4f\xb4\xcd\xe3\x17\x8f\xe6\x89\xd6>\xe39\xd4'
    SQLALCHEMY_DATABASE_URI = f"sqlite:///students.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Development(Config):
    Debug = True
 
class Testing:
    pass

config = {
    "development":Development
}