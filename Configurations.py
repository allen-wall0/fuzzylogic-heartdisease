# Configurations.py (No Changes - provided for completeness)
# Import Library
from numpy import *
import skfuzzy as fuzz
import skfuzzy.membership as mf
import matplotlib.pyplot as plt

# Start Define Inputs And Output Varietals

# Input
age                     = arange(0, 101, 1)
bloodPressure           = arange(0, 221, 1)
cholesterol             = arange(100, 251, 1)
bloodSugar              = arange(0, 121, 1)
highDensityLipoprotein  = arange(0, 71, 1)
lowDensityLipoprotein  = arange(0, 191, 1)

# Output
risk = arange(0, 46, 1)


def getInformationUser(mass):
    getVal = int(input(mass))
    return getVal
