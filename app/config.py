import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    # для генерации csrf-token в формах flask-wtf
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret'
    DEBUG = True
