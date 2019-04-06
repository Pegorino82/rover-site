from app import app
from mainapp.blueprint import main

# тут будем подключать Blueprints (приложения)
app.register_blueprint(main, url_prefix='/')

if __name__ == '__main__':
    app.run()
