from abc import ABC, abstractmethod
from Configurations import *
class IRuleBase(ABC):

    def __init__(self):
        pass

    def trapezoidalMembership(self):
        pass

    def triangularMembership(self):
        pass
    def draw(self):
        pass

    def membershipDegrees(self, userInput):
        pass