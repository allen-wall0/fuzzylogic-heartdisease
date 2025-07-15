from RuleBase.IRuleBase import *
from Configurations import *


class Cholesterol(IRuleBase):
    def __init__(self):
        super().__init__()
        self.cholesterolLow    = None
        self.cholesterolMid    = None
        self.cholesterolHigh   = None
        self.cholesterolFitLow = self.cholesterolFitMid = self.cholesterolFitHigh = None
        self.figure, self.cholesterol = plt.subplots(nrows=1)

    def trapezoidalMembership(self):
        self.cholesterolLow = mf.trapmf(cholesterol, [-30, -5, 180, 200])
        self.cholesterolMid = mf.trapmf(cholesterol, [180, 200, 220, 240])
        self.cholesterolHigh = mf.trapmf(cholesterol, [220, 240, 250, 270])

    def draw(self):
        self.cholesterol.plot(cholesterol, self.cholesterolLow, 'r', linewidth=2, label="Cholesterol Low")
        self.cholesterol.plot(cholesterol, self.cholesterolMid, 'g', linewidth=2, label="Cholesterol Mid")
        self.cholesterol.plot(cholesterol, self.cholesterolHigh, 'b', linewidth=2, label="cholesterolHigh")
        self.cholesterol.set_title("Cholesterol Rule")
        self.cholesterol.legend()
        plt.xlabel("Cholesterol Value")
        plt.ylabel("Member Ship Function")
        plt.show()

    def membershipDegrees(self, userCholesterol):
        self.cholesterolFitLow = fuzz.interp_membership(cholesterol, self.cholesterolLow, userCholesterol)
        self.cholesterolFitMid = fuzz.interp_membership(cholesterol, self.cholesterolMid, userCholesterol)
        self.cholesterolFitHigh = fuzz.interp_membership(cholesterol, self.cholesterolHigh, userCholesterol)