import os
import json
import sys

class ConfigFile:
    def __init__(self, filepath, *args):
        self.newArray = []
        self.path = filepath
    
    def __openConfig__(self, path):
        _path = path
        _pathSplit = path.split('/')
        _lengthOfPath = len(_pathSplit)
        try:
            if(_lengthOfPath > 1 and _lengthOfPath == 2):
                os.chdir(_pathSplit[0] + "/")
                configFile = open(_pathSplit[1], "r+")
                print("inside config file: \n", configFile.read())
                return configFile
        except:
            print("config file error: ", sys.exc_info())
        

    def __saveNewConfig__(self, newArray, path):
        _newArray = newArray
        _file = self.__openConfig__(path)
        _file.write(_newArray)
        print("New Array Saved: \n", _file.read())
        _file.close()

    def save(self):
        pass

    def read():
        pass

    def new():
        pass

    def edit():
        pass

    def _arrayarizer(arr):
        return arr

