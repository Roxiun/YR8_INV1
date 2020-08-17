import os
import sys
import math
import json
# Standard Imports + Math Import

sys.path.insert(1, os.path.join(sys.path[0], '..'))
# Make File run form the high directory

from utils.main import ReferenceNumbers
from utils.data import ref
# Code Handler Imports


# PyQt5 (UI Framework) Imports
from PyQt5 import QtWidgets, uic, QtGui


class StartUi(QtWidgets.QMainWindow):
    def __init__(self):
        '''View Initialisation'''
        super(StartUi, self).__init__()
        uic.loadUi('app/auto.ui', self)
        self.setWindowTitle('Photography Program')
        # Initialises the window

        self.aperture_button = self.findChild(QtWidgets.QCommandLinkButton, 'aperture_button')
        self.aperture_button.clicked.connect(self.start_aperture)
        self.shutter_button = self.findChild(QtWidgets.QCommandLinkButton, 'shutter_button')
        self.shutter_button.clicked.connect(self.start_shutter)

        self.show()
    
    def start_aperture(self):
        os.system(f"{sys.executable} python/semi_aperture.py")
    def start_shutter(self):
        os.system(f"{sys.executable} python/semi_shutter.py")
    

app = QtWidgets.QApplication(sys.argv)
window = StartUi()
app.exec_()