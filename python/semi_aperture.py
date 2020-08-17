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


class ProgramUi(QtWidgets.QMainWindow):
    def __init__(self):
        '''View Initialisation'''
        super(ProgramUi, self).__init__()
        uic.loadUi('app/semi_aperture.ui', self)
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

        self.result_lighting = self.findChild(QtWidgets.QLabel, 'answer_lighting')
        self.result_iso = self.findChild(QtWidgets.QLabel, 'answer_iso')
        self.result_shutter = self.findChild(QtWidgets.QLabel, 'answer_shutter')
        self.result_aperture = self.findChild(QtWidgets.QLabel, 'answer_aperture')


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
            ReferenceValues = self.ReferenceHandler.getAllReferenceValues(tdict)
            CurrentAverage = sum(ReferenceValues.values())
            RequiredAverage = 16

            SelectedValue = RequiredAverage-CurrentAverage

            selected = self.setting_type.currentText()
            selected = selected.replace(" Speed", "")
            selected = selected.replace(" Condition", "")
            
            if SelectedValue > 0 and SelectedValue <= 8:
                print(f"Required {self.setting_type.currentText()} Value: {ref[str(SelectedValue)][selected]}")
                tdict[self.setting_type.currentText()] = ref[str(SelectedValue)][selected]
                for item in tdict:
                    item_type = item.replace(" Speed", "").replace(" Condition", "")
                    
                    if self.ReferenceHandler.isValid(tdict[item], item_type):
                        if item == "ISO":
                            self.result_iso.setText(f"<b>{item}:</b> {tdict[item]}")
                        elif item == "Aperture":
                            self.result_aperture.setText(f"<b>{item}:</b> f/{tdict[item]}")
                        elif item_type == "Shutter":
                            self.result_shutter.setText(f"<b>{item}:</b> {tdict[item]}s")
                        elif item == "Lighting Condition":
                            self.result_lighting.setText(f"<b>Lighting Condition:</b> {tdict[item]}")
                    else:
                        if item == "ISO":
                            self.result_iso.setText(f"<b>{item}:</b> None")
                        elif item == "Aperture":
                            self.result_aperture.setText(f"<b>{item}:</b> None")
                        elif item_type == "Shutter":
                            self.result_shutter.setText(f"<b>{item}:</b> None")
                        elif item_type == "Lighting":
                            self.result_lighting.setText(f"<b>Lighting Condition:</b> None")
                return
            elif SelectedValue < 0:
                self.show_error(f"Too Bright", f"Change of {(SelectedValue - 1)*(-1)} stops is required")
                print(f"Too Bright - Change of {(SelectedValue - 1)*(-1)} stops is required")
            elif SelectedValue > 8:
                self.show_error(f"Too Dark", f"Change of {SelectedValue - 8} stops is required")
                print(f"Too Dark - Change of {SelectedValue - 8} stops is required")
            elif SelectedValue == 0:
                self.show_error(f"Error", f"You need to change you settings by 1 stop")
                print(f"You need to change you settings by 1 stop")


        else:
            tdict = {}

            tdict[self.CURRENT_LABELS[0]] = self.setting1_input.toPlainText().replace("f/", "").replace(".0", "").replace("ISO", "")
            tdict[self.CURRENT_LABELS[1]] = self.setting2_input.toPlainText().replace("f/", "").replace(".0", "").replace("ISO", "")
            tdict[self.CURRENT_LABELS[2]] = self.setting3_input.toPlainText().replace("f/", "").replace(".0", "").replace("ISO", "")
            for item in tdict:
                item_type = item.replace(" Speed", "").replace(" Condition", "")
                
                if self.ReferenceHandler.isValid(tdict[item], item_type):
                    if item == "ISO":
                        self.result_iso.setText(f"<b>{item}:</b> {tdict[item]}")
                    elif item == "Aperture":
                        self.result_aperture.setText(f"<b>{item}:</b> f/{tdict[item]}")
                    elif item_type == "Shutter":
                        self.result_shutter.setText(f"<b>{item}:</b> {tdict[item]}s")
                    elif item == "Lighting Condition":
                       self.result_lighting.setText(f"<b>Lighting Condition:</b> {tdict[item]}")
                else:
                    if item == "ISO":
                        self.result_iso.setText(f"<b>{item}:</b> None")
                    elif item == "Aperture":
                        self.result_aperture.setText(f"<b>{item}:</b> None")
                    elif item_type == "Shutter":
                        self.result_shutter.setText(f"<b>{item}:</b> None")
                    elif item_type == "Lighting":
                       self.result_lighting.setText(f"<b>Lighting Condition:</b> None")

    def show_error(self, title, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        x = msg.exec_()


app = QtWidgets.QApplication(sys.argv)
window = ProgramUi()
app.exec_()