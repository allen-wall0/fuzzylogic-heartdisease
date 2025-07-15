from RuleBase.IRuleBase import *
from Configurations import *

class RiskRule(IRuleBase):
    def __init__(self):
        super().__init__()
        self.riskNot        = None
        self.riskLittle     = None
        self.riskMid        = None
        self.riskHigh       = None
        self.riskVeryHigh   = None
        self.figure, self.risk = plt.subplots(nrows=1)


    def trapezoidalMembership(self):
        self.riskNot = mf.trapmf(risk, [0, 0, 5, 10])
        self.riskLittle = mf.trapmf(risk, [5, 10, 15, 20])
        self.riskMid = mf.trapmf(risk, [15, 20, 25, 30])
        self.riskHigh = mf.trapmf(risk, [25, 30, 35, 40])
        self.riskVeryHigh = mf.trapmf(risk, [35, 40, 45, 50])

    def draw(self):
        self.risk.plot(risk, self.riskNot, 'r', linewidth=2, label="Not Risk")
        self.risk.plot(risk, self.riskLittle, 'g', linewidth=2, label="Risk Little")
        self.risk.plot(risk, self.riskMid, 'b', linewidth=2, label="Risk Mid")
        self.risk.plot(risk, self.riskHigh, 'y', linewidth=2, label="Risk High")
        self.risk.plot(risk, self.riskVeryHigh, 'orange', linewidth=2, label="Risk Very High")
        self.risk.set_title("Risk Degree")
        self.risk.legend()
        plt.xlabel("Risk Value")
        plt.ylabel("Member Ship Function")
        plt.show()