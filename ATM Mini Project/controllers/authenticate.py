from utils import prompts
from views.menu import Menu
from utils.validators import Validation
from models.db import Database
from utils import queries
from helpers.input_functions import InputFunctions
from helpers import config
from utils.user_data import logged_in_user


class Authenticate:

    def __init__(self, unique_id = None, security_code = None):
        self.unique_id = unique_id
        self.security_code = security_code
       

    def check_credentials(self):
        valid_user = Database.get_item(queries.SEARCH_USER_DETAILS_IN_AUTH, self.unique_id, self.security_code,)
        return valid_user is not None
    
    
    def check_role(self):
        role = Database.get_item(queries.SEARCH_USER_DETAILS_IN_AUTH, self.unique_id, self.security_code)
        return role[2] == 'Admin'   
   

    def login():
        print(prompts.WELCOME)
        unique_id = InputFunctions.unique_id_input()
        while Validation.validate_id(unique_id) == False:
            unique_id = InputFunctions.valid_unique_id_input()
            
        security_code = InputFunctions.security_code_input()
        logged_in_user["unique_id"] = unique_id 
        
        user = Authenticate(unique_id, security_code)  
        if Authenticate.check_credentials(user):
            while True:
                try:
                    if Authenticate.check_role(user):
                        Menu.admin_menu()
                    else:
                        Menu.customer_menu()
                            
                except KeyError:
                    print(config.WRONG_INPUT)
        else:
            print(config.WRONG_CREDENTIALS)