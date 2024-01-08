from models.db import Database
from configurations import queries


class Authenticate:

    def __init__(self, **auth_details):
        self.unique_id = auth_details.get('unique_id')
        self.security_code = auth_details.get('security_code')
        self.db = Database()
       

    def check_credentials(self):
        valid_user = self.db.get_item(queries.SEARCH_USER_DETAILS_IN_AUTH, (self.unique_id, self.security_code,))
        return valid_user is not None
    
    
    def check_role(self):
        role = self.db.get_item(queries.SEARCH_USER_DETAILS_IN_AUTH, (self.unique_id, self.security_code,))
        return role[2]  