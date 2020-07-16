import os
import sys
import math
import json
# Standard Imports + Math Import

from tkinter import * 
from tkinter import font
from tkinter import messagebox
# Standard tkiner Imports

from main import ReferenceNumbers
from data import ref

Lighting_Condition = "Cloudy"
Selected_ISO = "100"
Selected_ShutterSpeed = "1/2000"
Selected_Aperture = ""
SelectedSettings = {"Lighting":Lighting_Condition, "ISO":Selected_ISO, "Shutter":Selected_ShutterSpeed, "Aperture":Selected_Aperture}

ReferenceHandler = ReferenceNumbers()
ReferenceValues = ReferenceHandler.getAllReferenceValues(SelectedSettings)

RequiredAverage = ReferenceHandler.getRequiredAverage(Lighting_Condition)
CurrentAverage = sum(ReferenceValues.values())

SelectedValue = RequiredAverage-CurrentAverage

print(f"Required Aperture Value: f/{ref[str(SelectedValue)]['Aperture']}")



class MainWindow:
	def __init__(self):
		self.OPTIONS_template = ["ISO", "Shutter Speed", "Aperture"]

		root = Tk()

		Label(root, text="Photography Settings", font=("Helvetica", 20, "bold underline")).grid(row=0)

		selectionA = StringVar(root)
		selectionA.set(self.OPTIONS_template[0])

		self.selectionA_Type = OptionMenu(root, selectionA, *self.OPTIONS_template)
		self.selectionA_Entry = Entry(root)

		(self.selectionA_Type).grid(row=1, column=0)
		(self.selectionA_Entry).grid(row=1, column=1)

		selectionB = StringVar(root)
		selectionB.set(self.OPTIONS_template[0])

		self.selectionB_Type = OptionMenu(root, selectionB, *self.OPTIONS_template)
		self.selectionB_Entry = Entry(root)

		(self.selectionB_Type).grid(row=2, column=0)
		(self.selectionB_Entry).grid(row=2, column=1)

		root.mainloop()

mw = MainWindow()