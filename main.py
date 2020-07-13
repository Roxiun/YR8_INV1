import os
import sys
import math
import json
# Standard imports

from data import modes, ref

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
