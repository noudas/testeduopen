'''
This script is responsible for running the Flask application once it has been initialized and configured through the `create_app` function. 

Key components:
- `from Flask_App.app import create_app`: Imports the `create_app` function from the `Flask_App.app` module. This function is expected to set up and return a Flask application instance, complete with configurations such as database connections and route definitions.
- `app = create_app()`: Calls the `create_app` function to instantiate the Flask application. This step involves executing any pre-configurations defined within `create_app`, such as database table creations and route initializations.
- `if __name__ == "__main__":`: Checks if the script is being run directly (not imported). This is a common Python idiom to ensure that certain blocks of code only execute when the script is run directly, not when it's imported as a module.
  - `app.run(host="0.0.0.0", port=5000, debug=True)`: Runs the Flask application with specific parameters:
      - `host="0.0.0.0"`: Makes the server accessible externally, allowing connections from any IP address.
      - `port=5000`: Specifies the port number on which the server will listen for incoming requests.
      - `debug=True`: Enables debug mode, providing more verbose output in case of errors and automatically reloading the server upon code changes during development.

This script effectively starts the Flask application, making it accessible over the network at the specified host and port, with debugging enabled for easier development and troubleshooting.
'''

from Flask_App.app import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)