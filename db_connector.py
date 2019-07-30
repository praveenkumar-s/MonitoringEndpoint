import sqlite3
import time
import sys

class DataProvider():
    def __init__(self,filename):
        self.DB_Filename = filename
        self.instance = sqlite3.connect(self.DB_Filename)
    
    def get_cursor(self):
        try:
           self.instance = sqlite3.connect(self.DB_Filename)
           cursor = self.instance.cursor()
           return cursor
        except:           
            print(sys.exc_info()) 
            return None

    def execute(self ,query,  cursor):
        try:
            
            cursor.execute(query)
            
            data =  cursor.fetchall()
            
            self.instance.commit()
            self.instance.close()
            return data
        except:
            print(sys.exc_info())
            return None
    
    def __del__(self):
        self.instance.close()