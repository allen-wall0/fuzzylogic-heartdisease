
from RuleBase.IRuleBase import *
from Configurations import *

class BloodSugar(IRuleBase):
    def __init__(self):
        super().__init__()
        self.bloodSugarVeryHigh = self.bloodSugarFitVeryHigh = None
        self.figure, self.bloodSugar = plt.subplots(nrows=1)

    def triangularMembership(self):
        self.bloodSugarVeryHigh = mf.trimf(bloodSugar, [90, 120, 130])

    def draw(self):
        self.bloodSugar.plot(bloodSugar, self.bloodSugarVeryHigh, 'r', linewidth=2, label="Blood Sugar Very High")
        self.bloodSugar.set_title("Blood Sugar")
        self.bloodSugar.legend()
        plt.xlabel("Blood Sugar")
        plt.ylabel("Member Ship Function")
        plt.show()

    def membershipDegrees(self, userBloodSugar):
        self.bloodSugarFitVeryHigh = fuzz.interp_membership(bloodSugar, self.bloodSugarVeryHigh, userBloodSugar)

