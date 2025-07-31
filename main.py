from flask import Flask
from config import Config
from models import db


# aplicando configurações
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

# registrando blueprints

from routes.home import home_route
from routes.carrinho import carrinho_route

app.register_blueprint(carrinho_route)
app.register_blueprint(home_route)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)