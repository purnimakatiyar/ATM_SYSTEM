from configurations import queries
from models.db import Database
from datetime import datetime
from prettytable import PrettyTable
from configurations import prompts
import random

class Account:
    

    def __init__(self, **account_details):
        self.unique_id = account_details.get('unique_id')      
        self.db = Database()
    
    
    def view_balance(self):
        response = self.db.get_item(queries.SEARCH_USER_DETAILS_IN_ACCOUNT, (self.unique_id,))
        if response:
            balance = response[3]
            print(f"\nYou have balance: {balance}")
            
            
    def deposit_money(self, amount):
        transaction_type = "Deposit"
        transaction_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        while True:
            transaction_id = random.randint(1000, 9999)
            exists = self.db.get_item(queries.SEARCH_EXISTING_TRANSACTION_ID, (transaction_id,))[0]
            if not exists:
                break
        self.db.update_item(queries.UPDATE_ADD_BALANCE, (amount, self.unique_id,))
        self.db.insert_item(queries.INSERT_TRANSACTION, 
                            (transaction_id, self.unique_id, 
                            transaction_type, transaction_date_time, amount,))
        print(prompts.MONEY_DEPOSIT)
        

    def withdraw_money(self, amount):
        transaction_type = "Withdraw"
        transaction_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response = self.db.get_item(queries.SEARCH_USER_DETAILS_IN_ACCOUNT, (self.unique_id,))
        if response is not None:
            balance = float(response[3])
            amount = float(amount) 
            if balance < amount:
                print(prompts.INSUFFICIENT_BALANCE)
                return
        while True:
            transaction_id = random.randint(1000, 9999)
            exists = self.db.get_item(queries.SEARCH_EXISTING_TRANSACTION_ID, (transaction_id,))[0]
            if not exists:
                break
        self.db.update_item(queries.UPDATE_REDUCE_BALANCE, (amount, self.unique_id,))
        self.db.insert_item(queries.INSERT_TRANSACTION, 
                            (transaction_id, self.unique_id, 
                            transaction_type, transaction_date_time, amount,))
        print(prompts.MONEY_WITHDRAWN)
    
        
    def view_recent_transactions(self):
        result = self.db.get_items(queries.GET_RECENT_TRANSACTIONS, (self.unique_id,))   
        if result:
            table = PrettyTable()
            table.field_names = ["Transaction ID", "Unique Id", "Type", "Date/Time", "Amount"]
            for i, row in enumerate(result[-5:], start = 1):
                transaction_id, unique_id, transaction_type, transaction_date_time, amount = row
                table.add_row([transaction_id, unique_id, transaction_type, transaction_date_time, amount])
            table.align = "l" 
            table.max_width["Type"] = 15
            table.max_width["Date/Time"] = 19     
            print(prompts.RECENT_TRANSACTIONS)
            print(table)
        else:
            print(prompts.NO_RECENT_TRANSACTIONS)