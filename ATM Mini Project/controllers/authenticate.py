from configurations import menu_prompts
from views.menu import Menu
from utils.validators import Validation
from models.db import Database
from configurations import queries
from helpers.input_functions import InputFunctions
from configurations import prompts
from utils.user_data import logged_in_user


class Authenticate:

    def __init__(self, unique_id = None, security_code = None):
        self.unique_id = unique_id
        self.security_code = security_code
        self.menu = Menu()
        self.input = InputFunctions()
        self.db = Database()
       

    def check_credentials(self):
        valid_user = self.db.get_item(queries.SEARCH_USER_DETAILS_IN_AUTH, (self.unique_id, self.security_code,))
        return valid_user is not None
    
    
    def check_role(self):
        role = self.db.get_item(queries.SEARCH_USER_DETAILS_IN_AUTH, (self.unique_id, self.security_code,))
        return role[2]  
   

    def login(self):
        print(menu_prompts.WELCOME)
        unique_id = self.input.unique_id_input()
        while Validation.validate_id(unique_id) == False:
            unique_id = self.input.valid_unique_id_input()
            
        security_code = self.input.security_code_input()
        logged_in_user["unique_id"] = unique_id 
        
        user = Authenticate(unique_id, security_code)  
        if Authenticate.check_credentials(user):
            while True:
                role = Authenticate.check_role(user)
                if role == 'Admin':
                    self.menu.admin_menu()
                else:
                    self.menu.customer_menu()            
        else:
            print(prompts.WRONG_CREDENTIALS)