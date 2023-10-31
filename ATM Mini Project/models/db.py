import sqlite3



class Database:
    def __init__(self):
        ...
        
    def __enter__(self):
        self.connection = sqlite3.connect('userdb.db')
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()
        
          
    def get_item(query, *data):
        with Database() as cursor:
            try:
                cursor.execute(query, data)
                response = cursor.fetchone()
            except sqlite3.Error as error:
                print(error)
            return response


    def get_items(query, *data):
        with Database() as cursor:
            try:
                cursor.execute(query, data)
                response = cursor.fetchall()
            except sqlite3.Error as error:
                print(error)
            return response


    def insert_item(query, *data):
        with Database() as cursor:
            try:
                cursor.execute(query, data)
            except sqlite3.Error as error:
                print(error)


    def update_item(query, *data):
        with Database() as cursor:
            try:
                cursor.execute(query, data)
            except sqlite3.Error as error:
                print(error)
            
        
        


            


            
            