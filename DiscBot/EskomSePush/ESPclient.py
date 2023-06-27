import requests
from core import Config, DatabaseHandler

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
        url = self.REQUESTURLS['Areas_Search_Text']
        url = "https://developer.sepush.co.za/business/2.0/area?id=eskde-10-fourwaysext10cityofjohannesburggauteng&test=future"
        payload={}
        headers={
            "token": Config.Token
        }

        response: requests.Response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

    def getAreaSearch(self, text: str):
        url = self.REQUESTURLS['AreaInfo']
        url = "https://developer.sepush.co.za/business/2.0/areas_search?text=brackenfell"
        payload={}
        headers={
            "token": Config.Token
        }

        response: requests.Response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)

    ###### Database Requests ######
    # TODO Add methods to send requests to the database