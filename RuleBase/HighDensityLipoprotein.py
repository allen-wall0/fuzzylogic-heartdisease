from RuleBase.IRuleBase import *
from Configurations import *


class HighDensityLipoprotein(IRuleBase):
    def __init__(self):
        super().__init__()
        self.hdlLow     = None
        self.hdlMid     = None
        self.hdlHigh    = None
        self.hdlFitLow  = self.hdlFitMid = self.hdlFitHigh = None
        self.figure, self.HDL = plt.subplots(nrows=1)

    def triangularMembership(self):
        self.hdlLow     = mf.trapmf(highDensityLipoprotein, [0, 0, 30, 40])
        self.hdlMid     = mf.trapmf(highDensityLipoprotein, [30, 40, 50, 60])
        self.hdlHigh    = mf.trapmf(highDensityLipoprotein, [50, 60, 80, 80])
    def draw(self):
        self.HDL.plot(highDensityLipoprotein, self.hdlLow, 'r', linewidth=2, label="HDL Low")
        self.HDL.plot(highDensityLipoprotein, self.hdlMid, 'g', linewidth=2, label="HDL Mid")
        self.HDL.plot(highDensityLipoprotein, self.hdlHigh, 'b', linewidth=2, label="HDL High")
        self.HDL.set_title("High Density Lipoprotein")
        self.HDL.legend()
        plt.xlabel("Density Lipoprotein")
        plt.ylabel("Member Ship Function")
        plt.show()

    def membershipDegrees(self, userHighDensityLipoprotein):
        self.hdlFitLow  = fuzz.interp_membership(highDensityLipoprotein, self.hdlLow, userHighDensityLipoprotein)
        self.hdlFitMid  = fuzz.interp_membership(highDensityLipoprotein, self.hdlMid, userHighDensityLipoprotein)
        self.hdlFitHigh = fuzz.interp_membership(highDensityLipoprotein, self.hdlHigh, userHighDensityLipoprotein)