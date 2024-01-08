from views.menu import Menu
from models.db import Database

def main():
    Menu().login()
    Database().close()
    
if __name__ == '__main__':
    main()