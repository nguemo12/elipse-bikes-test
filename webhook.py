import requests
import json
from config import API_KEY,API_URL

def fetchDataFromAPI(api_link):
    api_response = {}
    request = requests.get(api_link)

    if request.status_code == 200 and request.content:
        api_response = {"data": json.loads(request.content), "message": "fetch data successfully !!!","code":request.status_code} 
    else:
        api_response = {"data": [], "message": "An error occured in fetching the data !!!","code":request.status_code}

    return api_response

def getAllStations():
    api_link = API_URL+"/stations?apiKey="+API_KEY
    response = fetchDataFromAPI(api_link)
    return response

def getStationsByContractName(contract_name):
    api_link = API_URL+"/stations?contract="+contract_name+"&apiKey="+API_KEY
    response = fetchDataFromAPI(api_link)
    return response

def getStationDetails(station_number,contract_name):
    api_link = API_URL+"/stations/"+station_number+"?contract="+contract_name+"&apiKey="+API_KEY
    response = fetchDataFromAPI(api_link)
    return response

def getContractsList():
    api_link = API_URL+"/contracts"+"?apiKey="+API_KEY
    response = fetchDataFromAPI(api_link)
    return response

def getPackListOfContract(contract_name):
    api_link = API_URL+"/contracts/"+contract_name+"/parks?apiKey="+API_KEY
    response = fetchDataFromAPI(api_link)
    return response

def getParkDetails(contract_name,park_number):
    api_link = API_URL+"/contracts/"+contract_name+"/parks/"+park_number+"?apiKey="+API_KEY
    response = fetchDataFromAPI(api_link)
    return response

