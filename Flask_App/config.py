from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):
    PLUGGY_CLIENT_ID = os.getenv("PLUGGY_CLIENT_ID")
    PLUGGY_CLIENT_SECRET = os.getenv("PLUGGY_CLIENT_SECRET")
    PLUGGY_API_BASE_URL = os.getenv("PLUGGY_API_BASE_URL")