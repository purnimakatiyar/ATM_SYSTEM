from helpers.input_functions import InputFunctions
from helpers import config
from utils import prompts

class Menu():

    def admin_menu():
        try:
            while True:
                print(prompts.ADMIN_MENU)
                choice = int(input())
                if choice == 1:
                    InputFunctions.customer_add_input()
                elif choice == 2:
                    InputFunctions.delete_customer_input()
                elif choice == 3:
                    InputFunctions.change_security_code_input()
                elif choice == 4:
                    exit()    
        except KeyError:
            print(config.WRONG_INPUT)


    def customer_menu():
        try:
            while True:
                print(prompts.CUSTOMER_MENU)
                choice = int(input())
                if choice == 1:
                    InputFunctions.view_balance()
                elif choice == 2:
                    InputFunctions.deposit_money_input()
                elif choice == 3:
                    InputFunctions.Withdraw_money_input()
                elif choice == 4:
                    InputFunctions.view_recent_transactions()
                elif choice == 5:
                    InputFunctions.change_security_code_input()
                elif choice == 6:
                    exit()
        except KeyError:
            print(config.WRONG_INPUT)
