from RuleBase.IRuleBase import *
from Configurations import *
class LoweDensityLipoprotein(IRuleBase) :
    def __init__(self):
        super().__init__()
        self.ldlNormal      = None
        self.ldlLimit       = None
        self.ldlHigh        = None
        self.ldlVeryHigh    = None
        self.ldlFitNormal = self.ldlFitLimit = self.ldlFitHigh = self.ldlFitVeryHigh = None
        self.figure, self.LDL = plt.subplots(nrows=1)

    def triangularMembership(self):
        self.ldlNormal      = mf.trimf(loweDensityLipoprotein, [0, 0, 100, ])
        self.ldlLimit       = mf.trimf(loweDensityLipoprotein, [100, 130, 160, ])
        self.ldlHigh        = mf.trimf(loweDensityLipoprotein, [130, 160, 190, ])
        self.ldlVeryHigh    = mf.trapmf(loweDensityLipoprotein, [160, 190, 200, 200])

    def draw(self):
        self.LDL.plot(loweDensityLipoprotein, self.ldlNormal, 'r', linewidth=2, label="LDL Normal")
        self.LDL.plot(loweDensityLipoprotein, self.ldlLimit, 'g', linewidth=2, label="LDL Limit")
        self.LDL.plot(loweDensityLipoprotein, self.ldlHigh, 'b', linewidth=2, label="LDL High")
        self.LDL.plot(loweDensityLipoprotein, self.ldlVeryHigh, 'orange', linewidth=2, label="LDL Very high")
        self.LDL.set_title("Lowe Density Lipoprotein")
        self.LDL.legend()
        plt.xlabel("Density Lipoprotein")
        plt.ylabel("Member Ship Function")
        plt.show()

    def membershipDegrees(self, userLoweDensityLipoprotein):
        self.ldlFitNormal = fuzz.interp_membership(loweDensityLipoprotein, self.ldlNormal, userLoweDensityLipoprotein)
        self.ldlFitLimit = fuzz.interp_membership(loweDensityLipoprotein, self.ldlLimit, userLoweDensityLipoprotein)
        self.ldlFitHigh = fuzz.interp_membership(loweDensityLipoprotein, self.ldlHigh, userLoweDensityLipoprotein)
        self.ldlFitVeryHigh = fuzz.interp_membership(loweDensityLipoprotein, self.ldlVeryHigh, userLoweDensityLipoprotein)