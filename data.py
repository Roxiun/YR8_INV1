import os
import sys
import math
import json
# Standard imports

modes = {"Portrait":"For shots with a single point of intrest", "Landscape":"For landscape shots", "Sports":"For shots with fast moving objects"}

with open('reference.json') as json_file:
    ref = json.load(json_file)