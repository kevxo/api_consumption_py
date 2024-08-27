import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get('API_KEY')

def get_data(location: str):
    url = f'https://api.weatherstack.com/current?access_key={API_KEY}'

    params = {
        "query": location,
        "units": "f"
    }

    req = requests.get(url, params=params)

    return req.json()



