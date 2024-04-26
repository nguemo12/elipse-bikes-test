from dotenv import dotenv_values

config = dotenv_values(".env")
API_KEY = config['API_KEY']
API_URL = config['API_URL']
PORT = config['PORT']
HOST = config['HOST']