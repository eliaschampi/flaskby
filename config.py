import os

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    SQLALCHEMY_DATABASE_URI = 'mysql://panda:5403@localhost/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False