from utils.logging import Logs
from controllers.authenticate import Authenticate
from models.db import Database

def main():
    log = Logs()
    Authenticate().login()
    Database().close()
    
if __name__ == '__main__':
    main()