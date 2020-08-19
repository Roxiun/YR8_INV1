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


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        '''View Initialisation'''
        super(Ui, self).__init__()
        uic.loadUi('basic.ui', self)
        self.setWindowTitle('Photography Program')
        # Initalises the window from the .ui file
        self.OPTIONS = ["Lighting Condition", "ISO", "Shutter Speed", "Aperture"]
        
        self.setting1_type = self.findChild(QtWidgets.QComboBox, 'setting1_Combo')
        self.setting2_type = self.findChild(QtWidgets.QComboBox, 'setting2_Combo')
        self.setting1_type.addItems(self.OPTIONS)
        self.setting2_type.addItems(self.OPTIONS)
        self.setting1_type.currentTextChanged.connect(self.on_combobox_changed1)
        self.setting2_type.currentTextChanged.connect(self.on_combobox_changed2)
        self.setting2_type.setCurrentIndex(1) 

        self.setting1_input = self.findChild(QtWidgets.QTextEdit, 'setting1_textEdit')
        self.setting2_input = self.findChild(QtWidgets.QTextEdit, 'setting2_textEdit')
        self.setting1_input.textChanged.connect(self.update)
        self.setting2_input.textChanged.connect(self.update)
        # Creates All the Inputs & Settings

        self.ReferenceHandler = ReferenceNumbers()
        # Creates the reference handler

        self.show()
    
    def getInputs(self):
        ''' Gets all Values from the UI '''
        if self.setting1_type.currentText() == self.setting2_type.currentText():
            pass
    
    def on_combobox_changed1(self, value):
        if self.setting1_type.currentText() == self.setting2_type.currentText():
            if self.setting1_type.currentText() == "Lighting Condition":
                self.setting2_type.setCurrentIndex(1)
                self.setting1_type.model().item(1).setEnabled(False)
                self.setting1_type.model().item(0).setEnabled(True)
                self.setting2_type.model().item(0).setEnabled(False)
                self.setting2_type.model().item(1).setEnabled(True)
            else:
                self.setting2_type.setCurrentIndex(0)
                self.setting1_type.model().item(0).setEnabled(False)
                self.setting1_type.model().item(1).setEnabled(True)
                self.setting2_type.model().item(1).setEnabled(False)
                self.setting2_type.model().item(0).setEnabled(True)
        else:
            for i in range(len(self.OPTIONS)):
                self.setting2_type.model().item(i).setEnabled(True)
            self.setting2_type.model().item(self.setting1_type.currentIndex()).setEnabled(False)

    def on_combobox_changed2(self, value):
        if self.setting2_type.currentText() == self.setting1_type.currentText():
            if self.setting2_type.currentText() == "Lighting Condition":
                self.setting1_type.setCurrentIndex(1)
                self.setting2_type.model().item(1).setEnabled(False)
                self.setting2_type.model().item(0).setEnabled(True)
                self.setting1_type.model().item(0).setEnabled(False)
                self.setting1_type.model().item(1).setEnabled(True)
            else:
                self.setting1_type.setCurrentIndex(0)
                self.setting2_type.model().item(0).setEnabled(False)
                self.setting2_type.model().item(1).setEnabled(True)
                self.setting1_type.model().item(1).setEnabled(False)
                self.setting1_type.model().item(0).setEnabled(True)
        else:
            for i in range(len(self.OPTIONS)):
                self.setting1_type.model().item(i).setEnabled(True)
            self.setting1_type.model().item(self.setting2_type.currentIndex()).setEnabled(False)

    def update(self):       
        if self.setting1_type.currentText() != self.setting2_type.currentText():
            if self.setting1_input.toPlainText() != "" and self.setting2_input.toPlainText() != "":
                print(self.setting1_input.toPlainText())
                print(self.setting2_input.toPlainText())

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()