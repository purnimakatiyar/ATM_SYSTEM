from utils import queries
from models.db import Database
from utils.user_data import logged_in_user
from datetime import datetime
from prettytable import PrettyTable
from utils.logging import Logs
from helpers import config
from functools import wraps
import random

class Customer:

    def __init__(self, unique_id = None, security_code = None, account_number= None, 
                 name = None, balance = None, account_type = None):
        self.unique_id = unique_id
        self.security_code = security_code        
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.account_type = account_type
       
   
    def view_balance(self):
        response = Database.get_item(queries.SEARCH_USER_DETAILS_IN_ACCOUNT, logged_in_user["unique_id"])
        if response is not None:
            balance = response[3]
            print(f"\nYou have balance: {balance}")
            
            
    def deposit_money(self, amount):
        transaction_type = "Deposit"
        transaction_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while True:
            transaction_id = random.randint(1000, 9999)
            exists = Database.get_item(queries.SEARCH_EXISTING_TRANSACTION_ID, transaction_id)[0]
            if not exists:
                break
        Database.update_item(queries.UPDATE_ADD_BALANCE, amount, logged_in_user["unique_id"])
        Database.insert_item(queries.INSERT_TRANSACTION, transaction_id, logged_in_user["unique_id"], 
                                 transaction_type, transaction_date_time, amount)
        Logs.deposit_money(self)
        print(config.MONEY_DEPOSIT)
        

    def withdraw_money(self, amount):
        transaction_type = "Withdraw"
        transaction_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = Database.get_item(queries.SEARCH_USER_DETAILS_IN_ACCOUNT, logged_in_user["unique_id"])
        if response is not None:
            balance = float(response[3])
            amount = float(amount) 
            if balance < amount:
                print(config.INSUFFICIENT_BALANCE)
                return
        while True:
            transaction_id = random.randint(1000, 9999)
            exists = Database.get_item(queries.SEARCH_EXISTING_TRANSACTION_ID, transaction_id)[0]
            if not exists:
                break
        Database.update_item(queries.UPDATE_REDUCE_BALANCE, amount, logged_in_user["unique_id"])
        Database.insert_item(queries.INSERT_TRANSACTION, transaction_id, logged_in_user["unique_id"], 
                                transaction_type, transaction_date_time, amount)
        Logs.withdraw_money(self)
        print(config.MONEY_WITHDRAWN)
    
    
    def change_security_code(self, new_security_code):
        Database.update_item(queries.UPDATE_SECURITY_CODE_IN_AUTH, new_security_code, logged_in_user["unique_id"])
        Logs.change_security_code(self)
        
        
    def view_recent_transactions(self):
        result = Database.get_items(queries.GET_RECENT_TRANSACTIONS, logged_in_user["unique_id"])   
        if result:
            table = PrettyTable()
            table.field_names = ["Transaction ID", "Unique Id", "Type", "Date/Time", "Amount"]
            for i, row in enumerate(result[-5:], start = 1):
                transaction_id, unique_id, transaction_type, transaction_date_time, amount = row
                table.add_row([transaction_id, unique_id, transaction_type, transaction_date_time, amount])
            table.align = "l" 
            table.max_width["Type"] = 15
            table.max_width["Date/Time"] = 19     
            print(config.RECENT_TRANSACTIONS)
            print(table)
        else:
            print(config.NO_RECENT_TRANSACTIONS)
        
      
        

            
            
            
            
   
            
    
            
            
    
    
        
    
    
