import logging
from utils.user_data import logged_in_user

class Logs:
   
    def __init__(self):
        logging.basicConfig(filename='file.log', level=logging.INFO)
       
    def deposit_money(self):
        logging.info('Customer with id %r has deposited money successfully!',logged_in_user["unique_id"])
        
    def withdraw_money(self):
        logging.info('Customer with id %r has withdrawn money successfully!',logged_in_user["unique_id"])
        
    def change_security_code(self):
        logging.info('User with id %r has changed security code successfully!',logged_in_user["unique_id"])
        
    def user_exist(self):
        logging.error("User with user_id %r already exists but was trying to get added again. ",logged_in_user["unique_id"])
           
    def user_not_exist(self):
        logging.error("User with user_id %r does not exists but was trying to get removed. ",logged_in_user["unique_id"])
       
    def add_customer(self):
        logging.info('User with id %r has been added!',logged_in_user["unique_id"])
        
    def remove_customer(self):
        logging.info('User with id %r has been removed!',logged_in_user["unique_id"])
        