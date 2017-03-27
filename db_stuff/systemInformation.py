'''
Helper methods to determine what system we're on
apt-get vs brew
Instantiate this in the katoolinAppsInstall package so that it knows which version and for which OS to do its thing.
'''


import platform

def getOSInfo():
    operatingSystem = platform.system()
    return operatingSystem