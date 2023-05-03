import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    baseUrl = os.getenv("baseUrl")


config = Config()













