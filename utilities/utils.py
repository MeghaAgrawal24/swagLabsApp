import configparser

config= configparser.RawConfigParser() # This will help us to read data from ini file
config.read(".\\Configurtions\\config.ini")

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('common data', 'baseURL')
        return url

    @staticmethod
    def getApplicationUsername():
        username = config.get('common data', 'username')
        return username

    @staticmethod
    def getApplicationPassword():
        password = config.get('common data', 'password')
        return password

    @staticmethod
    def getApplicationFirstName():
        firstname = config.get('common data', 'firstname')
        return firstname

    @staticmethod
    def getApplicationLastName():
        lastname = config.get('common data', 'lastname')
        return lastname    



