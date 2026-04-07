from importlib.util import find_spec
requirements = ["numpy", "pandas", "requests", "matplotlib"]
for libs in requirements:
    if find_spec(libs) is None:
        print("Error")
    else:
        print()

# def checking_dependencies():

import matplolib
import numpy
import requests
import sys
import pandas