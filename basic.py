import os
import sys
import math
import json
# Standard Imports + Math Import

from main import ReferenceNumbers
from data import ref

Lighting_Condition = "Overcast"
Selected_ISO = "800"
Selected_ShutterSpeed = "1/2000"
Selected_Aperture = ""
SelectedSettings = {"Lighting":Lighting_Condition, "ISO":Selected_ISO, "Shutter":Selected_ShutterSpeed, "Aperture":Selected_Aperture}

ReferenceHandler = ReferenceNumbers()
ReferenceValues = ReferenceHandler.getAllReferenceValues(SelectedSettings)

RequiredAverage = ReferenceHandler.getRequiredAverage(Lighting_Condition)
CurrentAverage = sum(ReferenceValues.values())

SelectedValue = RequiredAverage-CurrentAverage

print(f"Required Aperture Value: f/{ref[str(SelectedValue)]['Aperture']}")