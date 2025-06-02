import os
from dotenv import load_dotenv

load_dotenv()

INTERNAL_API_KEY = os.getenv("INTERNAL_API_KEY")
API_KEY_METRO_CUADRADO = os.getenv("API_KEY_METRO_CUADRADO")

