import os
import sys
import math
import json
# Standard Imports + Math Import

from utils.main import ReferenceNumbers
from utils.data import ref

Lighting_Condition = "Lightly Cloudy"
Selected_ISO = "400"
Selected_ShutterSpeed = "1/125"
Selected_Aperture = ""
SelectedSettings = {"Lighting":Lighting_Condition, "ISO":Selected_ISO, "Shutter":Selected_ShutterSpeed, "Aperture":Selected_Aperture}

ReferenceHandler = ReferenceNumbers()
ReferenceValues = ReferenceHandler.getAllReferenceValues(SelectedSettings)

CurrentAverage = sum(ReferenceValues.values())
RequiredAverage = 16


SelectedValue = RequiredAverage-CurrentAverage

print(f"Required Aperture Value: f/{ref[str(SelectedValue)]['Aperture']}")