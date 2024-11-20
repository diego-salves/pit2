import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:9604@localhost/cakemania')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
