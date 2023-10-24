import requests
import os
from pprint import pprint 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY_FOR_WEATHER')



web = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q=Kamoke&appid={api_key}&units=imperial').json()

pprint(web['main']['temp'])