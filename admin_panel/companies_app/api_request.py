import requests
import pprint


response = requests.get('http://127.0.0.1:8000/companies_api/companies_api/')
pprint.pprint(response.json())