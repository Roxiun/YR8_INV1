import os
import sys
import math
import json
# Standard Imports + Math Import

from utils.main import ReferenceNumbers
from utils.data import ref
# Code Handler Imports

sys.path.insert(1, os.path.join(sys.path[0], '..'))
# Make File run form the high directory

# PyQt5 (UI Framework) Imports
from PyQt5 import QtWidgets, uic, QtGui


class StartUi(QtWidgets.QMainWindow):
    def __init__(self):
        '''View Initialisation'''
        super(StartUi, self).__init__()
        uic.loadUi('app/auto.ui', self)
        self.setWindowTitle('Photography Program')
        # Initialises the window

        self.portrait_button = self.findChild(QtWidgets.QCommandLinkButton, 'portrait_button')
        self.portrait_button.clicked.connect(self.start_portrait)
        self.sports_button = self.findChild(QtWidgets.QCommandLinkButton, 'sports_button')
        self.sports_button.clicked.connect(self.start_sports)

        self.show()
    
    def start_portrait(self):
        os.system(f"{sys.executable} python/auto_portrait.py")
    def start_sports(self):
        os.system(f"{sys.executable} python/auto_sports.py")
    

app = QtWidgets.QApplication(sys.argv)
window = StartUi()
app.exec_()