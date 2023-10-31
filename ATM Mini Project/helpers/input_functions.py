from controllers.admin import Admin
from controllers.customer import Customer
from utils.validators import Validation
from helpers import config

import maskpass

class InputFunctions:
    
    def customer_add_input():
        unique_id = input(config.UNIQUE_ID)
        while Validation.validate_id(unique_id) == False:
            unique_id = input(config.VALID_UNIQUE_ID)
             
        security_code = maskpass.advpass(prompt = config.SECURITY_CODE, mask = "*")
       

        account_number = input(config.ACCOUNT_NUMBER)
        while Validation.validate_account_number(account_number) == False:
            account_number = input(config.VALID_ACCOUNT_NUMBER)
        
        name = input(config.NAME)    
        while Validation.validate_account_number(account_number) == False:
            name = input(config.VALID_NAME)
            
        balance = input(config.BALANCE)

        account_type = input(config.ACCOUNT_TYPE)
        while Validation.validate_account_type(account_number) == True:
            account_type = input(config.VALID_ACCOUNT_TYPE)

        customer = Customer(unique_id, security_code, account_number, name, balance, account_type)
        Admin.add_customer(customer)
        
    
    def delete_customer_input():
        unique_id = input(config.DELETE_CUSTOMER)
        admin = Admin()
        admin.remove_customer(unique_id)
        
    def unique_id_input():
        return input(config.AUTH_UNIQUE_ID) 
    
    def security_code_input():
        return maskpass.advpass(prompt = config.AUTH_SECURITY_CODE, mask = "*")
        
    def valid_unique_id_input():
        unique_id = input(config.VALID_UNIQUE_ID)
        return unique_id 
        
    def deposit_money_input():
        amount = input(config.DEPOSIT_AMOUNT)
        customer = Customer()
        customer.deposit_money(amount)
        
    def Withdraw_money_input():
        amount = input(config.WITHDRAW_AMOUNT)
        customer = Customer()
        customer.withdraw_money(amount)
        
    def view_balance():
        customer = Customer()
        customer.view_balance()
  
    def change_security_code_input():
        new_security_code = maskpass.advpass(prompt = config.NEW_SECURITY_CODE, mask = "*")
        customer = Customer()
        customer.change_security_code(new_security_code)
        
    def view_recent_transactions():
        customer = Customer()
        customer.view_recent_transactions()
        
        
                