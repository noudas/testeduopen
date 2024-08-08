# Routes/__init__.py


from flask import Flask
from Flask_App.routes.transaction_routes import transaction_bp
from Flask_App.routes.person_routes import person_bp
from Flask_App.routes.connect_token_routes import connect_token_bp
from Flask_App.routes.connector_routes import connector_bp
from Flask_App.routes.item_routes import item_bp
from Flask_App.routes.account_routes import account_bp

def init_app():
    app = Flask(__name__)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(person_bp)
    app.register_blueprint(connect_token_bp)
    app.register_blueprint(connector_bp)
    app.register_blueprint(item_bp)
    app.register_blueprint(account_bp)
    return app
