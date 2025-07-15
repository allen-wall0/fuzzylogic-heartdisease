from RuleBase.IRuleBase import *
from Configurations import *
class LowDensityLipoprotein(IRuleBase) :
    def __init__(self):
        super().__init__()
        self.ldlNormal      = None
        self.ldlLimit       = None
        self.ldlHigh        = None
        self.ldlVeryHigh    = None
        self.ldlFitNormal = self.ldlFitLimit = self.ldlFitHigh = self.ldlFitVeryHigh = None
        self.figure, self.LDL = plt.subplots(nrows=1)

    def triangularMembership(self):
        self.ldlNormal      = mf.trimf(lowDensityLipoprotein, [0, 0, 100, ])
        self.ldlLimit       = mf.trimf(lowDensityLipoprotein, [100, 130, 160, ])
        self.ldlHigh        = mf.trimf(lowDensityLipoprotein, [130, 160, 190, ])
        self.ldlVeryHigh    = mf.trapmf(lowDensityLipoprotein, [160, 190, 200, 200])

    def draw(self):
        self.LDL.plot(lowDensityLipoprotein, self.ldlNormal, 'r', linewidth=2, label="LDL Normal")
        self.LDL.plot(lowDensityLipoprotein, self.ldlLimit, 'g', linewidth=2, label="LDL Limit")
        self.LDL.plot(lowDensityLipoprotein, self.ldlHigh, 'b', linewidth=2, label="LDL High")
        self.LDL.plot(lowDensityLipoprotein, self.ldlVeryHigh, 'orange', linewidth=2, label="LDL Very high")
        self.LDL.set_title("Low Density Lipoprotein")
        self.LDL.legend()
        plt.xlabel("Density Lipoprotein")
        plt.ylabel("Member Ship Function")
        plt.show()

    def membershipDegrees(self, userLowDensityLipoprotein):
        self.ldlFitNormal = fuzz.interp_membership(lowDensityLipoprotein, self.ldlNormal, userLowDensityLipoprotein)
        self.ldlFitLimit = fuzz.interp_membership(lowDensityLipoprotein, self.ldlLimit, userLowDensityLipoprotein)
        self.ldlFitHigh = fuzz.interp_membership(lowDensityLipoprotein, self.ldlHigh, userLowDensityLipoprotein)
        self.ldlFitVeryHigh = fuzz.interp_membership(lowDensityLipoprotein, self.ldlVeryHigh, userLowDensityLipoprotein)
