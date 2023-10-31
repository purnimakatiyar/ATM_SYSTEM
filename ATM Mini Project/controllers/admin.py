from controllers.customer import Customer
from models.db import Database
from utils import queries
from utils.logging import Logs
from helpers import config
from utils.user_data import logged_in_user

class Admin(Customer):
        
        
    def add_customer(self):
        count = Database.get_item(queries.SEARCH_EXISTING_USER_IN_AUTH, self.unique_id)[0]
        if count > 0:
            print(f"\nUser '{self.unique_id}' already exists.")
            Logs.user_exist(self)
        else:
            role = "Customer"
            Database.get_item(queries.INSERT_INTO_AUTH_TABLE, self.unique_id, self.security_code, role)
        Database.insert_item(queries.INSERT_INTO_ACCOUNT_TABLE,
                self.unique_id, self.account_number, self.name, self.balance, self.account_type)        
        print(config.ADDED_CUSTOMER)
        Logs.add_customer(self)


    def remove_customer(self, unique_id):
        while True:
            with Database() as cursor:
                cursor.execute(queries.SEARCH_EXISTING_USER_IN_ACCOUNT,(unique_id, ))
                count = cursor.fetchone()[0]
                if count > 0:
                    cursor.execute(queries.DELETE_FROM_ACCOUNT_TABLE,(unique_id, ))
                    print(config.REMOVED_CUSTOMER)
                    Logs.remove_customer(self)
                    break
                else:
                    print(config.USER_NOT_EXIST_REMOVE_CUSTOMER)
                    Logs.user_not_exist(self)
             
           
    def change_security_code(self, new_security_code):
        Database.update_item(queries.UPDATE_SECURITY_CODE_IN_AUTH, new_security_code, logged_in_user["unique_id"])
        Logs.change_security_code(self)
            
            

                    
                    
     
        

        
    
