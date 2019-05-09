import requests
from fai.config import FaiConfig as config


def getinvoicelistofperiod(period: str) -> 'list':
    URL = f'https://{config.fakt_domain}.fakturownia.pl/invoices.json?period={period}&api_token={config.fakt_token}'
    response = requests.get(URL)
    return response.json()


def getinvoicebyid(id: str):
    URL = f'https://{config.fakt_domain}.fakturownia.pl/invoices/{id}.json?api_token={config.fakt_token}'
    response = requests.get(URL)
    return response.json()


def getclientbyid(id: str):
    '''curl "https://YOUR_DOMAIN.fakturownia.pl/clients/100.json?api_token=API_TOKEN"'''
    URL = f'https://{config.fakt_domain}.fakturownia.pl/clients/{id}.json?api_token={config.fakt_token}'
    response = requests.get(URL)
    return  response.json()

def getinvoicebyiddotreplaced(id: str):
    URL = f'https://{config.fakt_domain}.fakturownia.pl/invoices/{id}.json?api_token={config.fakt_token}'
    response = requests.get(URL)
    return response.json()