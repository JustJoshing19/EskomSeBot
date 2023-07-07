import requests
from datetime import datetime
from .core import Config
from .core import DatabaseHandler
from asyncio import sleep

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
    def getLoadsheddingTimes(self) -> dict:
        data = self.DBHandler.getAllUsersLoadshedding()

        sortedData = {}

        for item in data:
            startTime = self.formatTime(item[1])
            endTime = self.formatTime(item[2])
            sortedData[item[3]] = [startTime, endTime]
        print(sortedData)

        return sortedData
    
    async def getAllAreas(self) -> list:
        await sleep(2)
        AreaList = self.DBHandler.getAllAreas()
        areas = []
        for i in range(0, AreaList.__len__()):
            item = AreaList[i]
            areas.append({'id':item[0], 'name':item[1]})
        return areas
    
    async def addUser(self, user: dict) -> bool:
        if not self.checkForUser(user['id']):
            self.DBHandler.addUser(user['id'], user['name'], user['area'])
            return True
        return False

    def checkForUser(self, id: str) -> bool:
        result: list = self.DBHandler.getUser(id)
        if result:
            return True
        return False


    ###### Util Methods ######
    def formatTime(self, times: str) -> str:
        times = times[:-6]
        times = times.replace("T", " ")
        times: datetime =  datetime.strptime(times, "%Y-%m-%d %H:%M:%S") 
        return times.strftime("%m-%d %H:%M")