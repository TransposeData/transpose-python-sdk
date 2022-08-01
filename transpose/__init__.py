import os
from os.path import join, dirname

from dotenv import load_dotenv
load_dotenv(join(dirname(__file__), '.env'))

print(os.environ)

api_key = os.environ.get("API_KEY")

# this file is important for nice imports
from .src.base import Transpose