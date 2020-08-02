import os
import sys
import math
import json
# Standard imports

from utils.data import modes, ref

class ReferenceNumbers:
	def __init__(self):
		pass
	def getReferenceValue(self, UserInput):
		if UserInput == "" : return 0	
		else:
			for number in ref: 
				for value in ref[number]:
					if ref[number][value] == UserInput:
						return int(number)
	def getRequiredAverage(self, UserInput):
		for number in ref: 
			for value in ref[number]:
				if ref[number][value] == UserInput:
					return int(number)*4
	def getAllReferenceValues(self, UserDict):
		'''
		Input is taken in the order of:
		Lighting Condition, ISO, Shutter Speed, Aperture
		'''
		tempDict = {}
		for setting in UserDict:
			tempDict[setting] = self.getReferenceValue(UserDict[setting])
		return tempDict
	
	def isValid(self, UserInput, UserType = None):
		if not UserType:
			for number in ref:
				for key in ref[number]:
					if ref[number][key] == UserInput:
						return True
			return False
		else:
			UserInput = UserInput.replace("ISO ", "")
			UserType = UserType.replace(" Speed", "")
			UserType = UserType.replace(" Condition", "")
			if UserType == "Shutter":
				UserInput = UserInput.replace("s", "")
			for number in ref:
				if ref[number][UserType] == UserInput:
					return True
			return False



class CameraModes:
	def __init__(self):
		pass
	def isValid(self, UserInput):
		for mode in modes:
			if UserInput == mode:
				return True
		return False
	def getDescription(self, UserInput):
		return modes[UserInput]
