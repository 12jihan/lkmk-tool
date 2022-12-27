import json
import os
import sys
from config import ConfigFile as cfile 
from guieditor import GUIEditor as gui
from PyQt6.QtCore import * 
from PyQt6.QtGui import * 
from PyQt6.QtWidgets import *

def main(): 
    print("Starting App...")
    config = cfile("assets/lkmk_config.json")
    App = QApplication(sys.argv)

    window = gui()
    sys.exit(App.exec())    
    

if __name__=="__main__":
    main()