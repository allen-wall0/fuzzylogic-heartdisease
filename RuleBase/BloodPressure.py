from RuleBase.IRuleBase import *
from Configurations import *

class BloodPressure(IRuleBase):
    def __init__(self):
        super().__init__()
        self.bloodPressureLow      = None
        self.bloodPressureMid      = None
        self.bloodPressureHigh     = None
        self.bloodPressureVeryHigh = None
        self.bloodPressureFitLow = self.bloodPressureFitMid = self.bloodPressureFitHigh = self.bloodPressureFitVeryHigh = None
        self.figure, self.bloodPressure = plt.subplots(nrows=1)

    def trapezoidalMembership(self):
        self.bloodPressureLow = mf.trapmf(bloodPressure, [-30, -5, 100, 120])
        self.bloodPressureMid = mf.trapmf(bloodPressure, [100, 120, 140, 160])
        self.bloodPressureHigh = mf.trapmf(bloodPressure, [140, 160, 180, 200])
        self.bloodPressureVeryHigh = mf.trapmf(bloodPressure, [180, 200, 220, 220])

    def draw(self):
        self.bloodPressure.plot(bloodPressure, self.bloodPressureLow, 'r', linewidth=2, label='Blood Pressure Low')
        self.bloodPressure.plot(bloodPressure, self.bloodPressureMid, 'g', linewidth=2, label='Blood Pressure Mid')
        self.bloodPressure.plot(bloodPressure, self.bloodPressureHigh, 'b', linewidth=2, label='Blood Pressure High')
        self.bloodPressure.plot(bloodPressure, self.bloodPressureVeryHigh, 'orange', linewidth=2, label='Blood Pressure Very High')
        self.bloodPressure.set_title("Blood Pressure")
        self.bloodPressure.legend()
        plt.xlabel("Blood Pressure")
        plt.ylabel("Member Ship Function")
        plt.show()

    def membershipDegrees(self, bloodPressureUser):
        self.bloodPressureFitLow = \
            fuzz.interp_membership(bloodPressure, self.bloodPressureLow, bloodPressureUser)
        self.bloodPressureFitMid = \
            fuzz.interp_membership(bloodPressure, self.bloodPressureMid, bloodPressureUser)
        self.bloodPressureFitHigh = \
            fuzz.interp_membership(bloodPressure, self.bloodPressureHigh, bloodPressureUser)
        self.bloodPressureFitVeryHigh = \
            fuzz.interp_membership(bloodPressure, self.bloodPressureVeryHigh, bloodPressureUser)