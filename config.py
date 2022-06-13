from dotenv import load_dotenv

load_dotenv()

import os

INTRO_USERNAME = os.getenv('INTRO_USERNAME')
INTRO_PASSWORD = os.getenv('INTRO_PASSWORD')