from configurations import queries
from models.db import Database
from configurations import prompts

class User:

    def __init__(self, **user_details):
        self.unique_id = user_details.get('unique_id')
        self.security_code = user_details.get('security_code')        
        self.account_number = user_details.get('account_number')
        self.name = user_details.get('name')
        self.balance = user_details.get('balance')
        self.account_type = user_details.get('account_type')
        self.db = Database()
        
        
    def add_customer(self):
        count = self.db.get_item(queries.SEARCH_EXISTING_USER_IN_AUTH, (self.unique_id,))[0]
        if count > 0:
            print(f"\nUser '{self.unique_id}' already exists.")
            
        else:

            self.db.get_item(queries.INSERT_INTO_AUTH_TABLE, (self.unique_id, self.security_code, prompts.ROLE,))
            self.db.insert_item(queries.INSERT_INTO_ACCOUNT_TABLE,
                             (self.unique_id, self.account_number, 
                              self.name, self.balance, self.account_type,))        
        print(prompts.ADDED_CUSTOMER)


    def remove_customer(self, unique_id):
        count = self.db.get_item(queries.SEARCH_EXISTING_USER_IN_ACCOUNT, (unique_id,))[0]
        if count > 0:
            self.db.update_item(queries.DELETE_FROM_ACCOUNT_TABLE, (unique_id,))
            print(prompts.REMOVED_CUSTOMER)
        else:
            print(prompts.USER_NOT_EXIST_REMOVE_CUSTOMER)
             
           
    def change_security_code(self, new_security_code):
        self.db.update_item(queries.UPDATE_SECURITY_CODE_IN_AUTH, (new_security_code, self.unique_id))
