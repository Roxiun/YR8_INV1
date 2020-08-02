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


class ProgramUi(QtWidgets.QMainWindow):
    def __init__(self):
        '''View Initialisation'''
        super(ProgramUi, self).__init__()
        uic.loadUi('app/basic.ui', self)
        self.setWindowTitle('Photography Program')
        # Initalises the window from the .ui file
        self.OPTIONS = ["Lighting Condition", "ISO", "Shutter Speed", "Aperture"]
        
        self.setting_type = self.findChild(QtWidgets.QComboBox, 'setting1_Combo')
        self.setting_type.addItems(self.OPTIONS)
        self.setting_type.currentTextChanged.connect(self.update_combo)

        self.settings1_label = self.findChild(QtWidgets.QLabel, 'value1_Label')
        self.settings2_label = self.findChild(QtWidgets.QLabel, 'value2_Label')
        self.settings3_label = self.findChild(QtWidgets.QLabel, 'value3_Label')

        self.setting1_input = self.findChild(QtWidgets.QTextEdit, 'setting1_textEdit')
        self.setting2_input = self.findChild(QtWidgets.QTextEdit, 'setting2_textEdit')
        self.setting3_input = self.findChild(QtWidgets.QTextEdit, 'setting3_textEdit')
        self.setting1_input.textChanged.connect(self.update)
        self.setting2_input.textChanged.connect(self.update)
        self.setting3_input.textChanged.connect(self.update)

        self.CURRENT_LABELS = list(self.OPTIONS)
        self.CURRENT_LABELS.remove(self.setting_type.currentText())
        # Creates All the Inputs & Settings

        self.ReferenceHandler = ReferenceNumbers()
        # Creates the reference handler

        self.show()
    

    def update_combo(self):
        tempDict = {}

        tempDict[self.CURRENT_LABELS[0]] = self.setting1_input.toPlainText()
        tempDict[self.CURRENT_LABELS[1]] = self.setting2_input.toPlainText()
        tempDict[self.CURRENT_LABELS[2]] = self.setting3_input.toPlainText()
            
        
        self.CURRENT_LABELS = list(self.OPTIONS)
        self.CURRENT_LABELS.remove(self.setting_type.currentText())
        self.settings1_label.setText("{}".format(self.CURRENT_LABELS[0]))
        self.settings2_label.setText("{}".format(self.CURRENT_LABELS[1]))
        self.settings3_label.setText("{}".format(self.CURRENT_LABELS[2]))

        if self.settings1_label.text() in tempDict:
            self.setting1_input.setText(tempDict[self.settings1_label.text()])
        else:
            self.setting1_input.setText("")
        
        if self.settings2_label.text() in tempDict:
            self.setting2_input.setText(tempDict[self.settings2_label.text()])
        else:
            self.setting2_input.setText("")
        
        if self.settings3_label.text() in tempDict:
            self.setting3_input.setText(tempDict[self.settings3_label.text()])
        else:
            self.setting3_input.setText("")
    
    def update(self):
        tdict = {}

        tdict[self.CURRENT_LABELS[0]] = self.setting1_input.toPlainText().replace("f/", "").replace(".0", "").replace("ISO", "")
        tdict[self.CURRENT_LABELS[1]] = self.setting2_input.toPlainText().replace("f/", "").replace(".0", "").replace("ISO", "")
        tdict[self.CURRENT_LABELS[2]] = self.setting3_input.toPlainText().replace("f/", "").replace(".0", "").replace("ISO", "")
        if self.ReferenceHandler.isValid(tdict[self.CURRENT_LABELS[0]], self.CURRENT_LABELS[0]) and self.ReferenceHandler.isValid(tdict[self.CURRENT_LABELS[1]], self.CURRENT_LABELS[1]) and self.ReferenceHandler.isValid(tdict[self.CURRENT_LABELS[2]], self.CURRENT_LABELS[2]):
            print(tdict)
            ReferenceValues = self.ReferenceHandler.getAllReferenceValues(tdict)
            print(ReferenceValues)
            CurrentAverage = sum(ReferenceValues.values())
            RequiredAverage = 16

            SelectedValue = RequiredAverage-CurrentAverage

            selected = self.setting_type.currentText()
            selected = selected.replace(" Speed", "")
            selected = selected.replace(" Condition", "")
            print(f"Required {self.setting_type.currentText()} Value: {ref[str(SelectedValue)][selected]}")
            tdict[self.setting_type.currentText()] = ref[str(SelectedValue)][selected]

app = QtWidgets.QApplication(sys.argv)
window = ProgramUi()
app.exec_()