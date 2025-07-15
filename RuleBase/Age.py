from RuleBase.IRuleBase import *
from Configurations import *
class Age(IRuleBase):
    def __init__(self):
        super().__init__()
        self.ageYoung = None
        self.ageMid = None
        self.ageOld = None
        self.ageFitYoung = self.ageFitMid = self.ageFitOld = None
        self.figure, self.ruleAge = plt.subplots(nrows=1)

    def trapezoidalMembership(self):
        self.ageYoung   = mf.trapmf(age, [-30, -5, 30, 40])
        self.ageMid     = mf.trapmf(age, [30, 40, 50, 60])
        self.ageOld     = mf.trapmf(age, [50, 60, 100, 100])

    def draw(self):
        self.ruleAge.plot(age, self.ageYoung, 'r', linewidth=2, label='Young')
        self.ruleAge.plot(age, self.ageMid, 'g', linewidth=2, label='Middle')
        self.ruleAge.plot(age, self.ageOld, 'b', linewidth=2, label='Old')
        self.ruleAge.set_title("Age Rule")
        self.ruleAge.legend()
        plt.xlabel("Age's")
        plt.ylabel("Member Ship Function")
        plt.show()

    def membershipDegrees(self, ageUser):
        self.ageFitYoung = fuzz.interp_membership(age, self.ageYoung, ageUser)
        self.ageFitMid   = fuzz.interp_membership(age, self.ageMid, ageUser)
        self.ageFitOld   = fuzz.interp_membership(age, self.ageOld, ageUser)