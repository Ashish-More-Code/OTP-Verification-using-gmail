Environment Variables
====================
pip install python-dotenv
======================


Create a .env file in your project root and add your sensitive information
===========
EMAIL_HOST_PASSWORD=your_email_password

Load environment variables in your settings.py:
===================
from dotenv import load_dotenv <p>
import os  <p>
load_dotenv()  <p>
# Load environment variables from .env file 
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
