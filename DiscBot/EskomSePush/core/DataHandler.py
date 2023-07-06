import sqlite3
import os

class DatabaseHandler():
    def __init__(self) -> None:
        BasePath = os.path.dirname(os.path.abspath(__file__))
        dbPath = os.path.join(BasePath, "AreaData.sqlite3")
        self.conn: sqlite3.Connection = sqlite3.connect(dbPath)
        self.cursor: sqlite3.Cursor
        print('Database opened')

    def exeSelect(self, query: str):
        self.cursor = self.conn.execute(query)
        print('Query Executed')

    def exeInsert(self, query: str):
        self.cursor = self.conn.execute(query)
        self.conn.commit()

    ###### Get & Add Methods ######
    def getAllAreas(self) -> list:
        query: str = "SELECT * from 'Areas'"
        self.exeSelect(query)
        return self.cursor.fetchall()

    def getArea(self, areaCode: str) -> list:
        query: str = "SELECT * from 'Areas' as a WHERE a.id = '" + areaCode + "'"
        self.exeSelect(query)
        return self.cursor.fetchall()
    
    def getAllUsers(self) -> list:
        query: str = "SELECT * from 'Users'"
        self.exeSelect(query)
        return self.cursor.fetchall()
    
    def getUser(self, id: str) -> list:
        query: str = "SELECT * from 'Users' as u WHERE u.id = '" + id + "'"
        self.exeSelect(query)
        return self.cursor.fetchall()
    
    def getAllLoadshedding(self) -> list:
        query: str = "SELECT * from 'Loadshedding'"
        self.exeSelect(query)
        return self.cursor.fetchall()
    
    def getLoadshedding(self, area: str) -> list:
        query: str = "SELECT * from Loadshedding as l WHERE l.area = '" + area + "'"
        self.exeSelect(query)
        return self.cursor.fetchall()
    
    def getAllUsersLoadshedding(self) -> list:
        query: str = "SELECT l.area, start, end, u.name, a.name from Loadshedding as l JOIN Users as u on l.area = u.area JOIN Areas as a on a.id = l.area"
        self.exeSelect(query)
        return self.cursor.fetchall()
    
    def addUser(self, id: str, name: str, area: str):
        query: str = 'INSERT INTO "Users" ("id", "name", "area") VALUES ("'+ id +'", "' + name + '", "' + area + '");'
        self.exeInsert(query)
        print(self.cursor.fetchall())