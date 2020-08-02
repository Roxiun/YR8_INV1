import os
import sys
import math
import json
# Standard Imports + Math Import

from utils.main import ReferenceNumbers
from utils.data import ref
# Code Handler Imports

# PyQt5 (UI Framework) Imports
from PyQt5 import QtWidgets, uic, QtGui


class StartUi(QtWidgets.QMainWindow):
    def __init__(self):
        '''View Initialisation'''
        super(StartUi, self).__init__()
        uic.loadUi('app/start.ui', self)
        self.setWindowTitle('Photography Program')
        # Initialises the window

        self.progam_button = self.findChild(QtWidgets.QCommandLinkButton, 'program_button')
        self.progam_button.clicked.connect(self.start_program)

        self.show()
    
    def start_program(self):
        os.system(f"{sys.executable} python/program.py")
    

app = QtWidgets.QApplication(sys.argv)
window = StartUi()
app.exec_()