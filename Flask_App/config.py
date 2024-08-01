# config,py
'''
It then defines a configuration class that retrieves specific environment variables related to Pluggy API credentials and base URL.

This script uses the `dotenv` package to load environment variables from a `.env` file into the system's environment variables.
Steps performed:
1. Imports `load_dotenv` from the `dotenv` package, which allows loading environment variables from a `.env` file.
2. Imports the built-in `os` module, providing access to the operating system's environment variables.
3. Calls `load_dotenv()`, ensuring that all environment variables defined in a `.env` file located at the root of the project are loaded into the system's environment variables.
4. Defines a class named `Config` that serves as a container for configuration settings.
   - Retrieves and assigns values for `PLUGGY_CLIENT_ID`, `PLUGGY_CLIENT_SECRET`, and `PLUGGY_API_BASE_URL` from the environment variables.
      - These variables are expected to be set in the `.env` file and represent credentials and the base URL needed to interact with the Pluggy API

Usage: Instances of the `Config` class can be created elsewhere in the application to access these configuration settings, facilitating secure and dynamic configuration management.
'''

from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    PLUGGY_CLIENT_ID = os.getenv("PLUGGY_CLIENT_ID")
    PLUGGY_CLIENT_SECRET = os.getenv("PLUGGY_CLIENT_SECRET")
    PLUGGY_API_BASE_URL = os.getenv("PLUGGY_API_BASE_URL")