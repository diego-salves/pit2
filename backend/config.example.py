import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/cakemania')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
