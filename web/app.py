from flask import Flask
from redis import Redis

def create_app(name='default'):
    app = Flask(name)
    return app

def create_extension(app):
    return app
