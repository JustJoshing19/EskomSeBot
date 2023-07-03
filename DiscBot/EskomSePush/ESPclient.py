import requests
from json import dumps
from .core import Config
from .core import DatabaseHandler

TESTING = False

class ESP_API_Client():
    TOKEN: str = Config.Token
    REQUESTURLS = {
        'Status': '',
        'AreaInfo':'https://developer.sepush.co.za/business/2.0/area',
        'AreasNearbyGPS':'',
        'Areas_Search_Text':'https://developer.sepush.co.za/business/2.0/areas_search',
        'TopicsNearby':'',
        'Checkallowance':'https://developer.sepush.co.za/business/2.0/api_allowance',
        }
    
    DBHandler = DatabaseHandler()

    ###### API Requests ######
    def getAllowance(self):
        url = self.REQUESTURLS['Checkallowance']
        payload={}
        headers={
            "token": Config.Token
        }

        response: requests.Response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

    def getAreaInfo(self, testing: bool, id: str):
        testRequest = ''
        if testing:
            testRequest = '&test=future'
        area = id

        url = self.REQUESTURLS['Areas_Search_Text']
        url = "https://developer.sepush.co.za/business/2.0/area?id=" + area + testRequest
        payload={}
        headers={
            "token": Config.Token
        }

        response: requests.Response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

    def getAreaSearch(self, text: str):
        url = self.REQUESTURLS['AreaInfo']
        url = "https://developer.sepush.co.za/business/2.0/areas_search?text=" + text
        payload={}
        headers={
            "token": Config.Token
        }

        response: requests.Response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

    ###### Database Requests ######
    # TODO Add methods to send requests to the database
    def getLoadsheddingTimes(self) -> dict:
        data = self.DBHandler.getAllUsersLoadshedding()

        sortedData = {}

        for item in data:
            sortedData[item[3]] = [item[1], item[2]]

        return sortedData
        print(sortedData)