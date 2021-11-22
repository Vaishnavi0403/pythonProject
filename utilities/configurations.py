import configparser


def getConfig():
    # creating config object to access configurable properties
    config = configparser.ConfigParser()
    # reading from properties.ini file
    config.read('utilities/properties.ini')
    return config

