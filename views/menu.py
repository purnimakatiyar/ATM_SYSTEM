from helpers.input_functions import InputFunctions
from controllers.user import User
from configurations import prompts
from configurations import menu_prompts

class Menu:
    
    def __init__(self):
        self.input = InputFunctions()
        self.user = User()


    def admin_menu(self):
        
        while True:
            print(menu_prompts.ADMIN_MENU)
                
            choice = int(input())
                
            if choice == 1:
                self.input.customer_add_input()
                
            elif choice == 2:
                unique_id = self.input.delete_customer_input()
                self.user.remove_customer(unique_id)
                
            elif choice == 3:
                new_security_code = self.input.change_security_code_input()
                self.user.change_security_code(new_security_code)
                
            elif choice == 4:
                exit()
            
            else:
                print(prompts.WRONG_INPUT)
       
            
    def customer_menu(self):
        
        while True:
            print(menu_prompts.CUSTOMER_MENU)
            choice = int(input())
            
            if choice == 1:
                self.user.view_balance()
                
            elif choice == 2:
                amount = self.input.deposit_money_input()
                self.user.deposit_money(amount)
        
            elif choice == 3:
                amount = self.input.Withdraw_money_input()
                self.user.withdraw_money(amount)
                    
            elif choice == 4:
                self.user.view_recent_transactions()
                    
            elif choice == 5:
                new_security_code = self.input.change_security_code_input()
                self.user.change_security_code(new_security_code)
                
            elif choice == 6:
                exit()
                
            else:
                print(prompts.WRONG_INPUT)