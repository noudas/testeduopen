from flask import Flask
from flask_cors import CORS
from .db_setup import initialize_database  # Import the initialize_database function from db_setup module
from .routes import init_app  # Import the route initialization function

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Initialize the database tables
    initialize_database()

    # Initialize and register routes
    init_app()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)