# Risk.py (No Changes - provided for completeness)
from RuleBase import *
from types import SimpleNamespace
from Configurations import *

class Risk:
    def __init__(self, **rules):
        # print(rules.keys())
        self.rules = SimpleNamespace(**rules)
        self.rule1 = self.rule2 = self.rule3 = self.rule3 = self.rule4 = self.rule4 = self.rule5 = self.rule6 = self.rule7\
            = self.rule8 = self.rule9 = self.rule10 = self.rule11 = self.rule12 = self.rule13 = self.rule14 = self.rule15 \
            = self.rule16 \
            = self.rule17 =self.rule18 = self.rule19 = self.rule20 = self.rule21 = self.rule22 = self.rule23 = self.rule24 = None
        self.uninfected = self.little = self.mid = self.high = self.veryHigh = None

    def inferenceSystems(self):
        self.rule1 = fmin(
            fmin(fmin(fmin(self.rules.bloodRule.bloodPressureFitLow, self.rules.cholesterolRule.cholesterolFitLow),
                      self.rules.ldlRule.ldlFitNormal), self.rules.hdlRule.hdlFitHigh), self.rules.riskRule.riskNot)

        self.rule2 = fmin(
            fmin(fmin(fmin(self.rules.bloodRule.bloodPressureFitLow, self.rules.cholesterolRule.cholesterolFitLow),
                      self.rules.ldlRule.ldlFitLimit), self.rules.hdlRule.hdlFitHigh),
            self.rules.riskRule.riskLittle)

        self.rule3 = fmin(
            fmin(fmin(fmin(self.rules.bloodRule.bloodPressureFitLow, self.rules.cholesterolRule.cholesterolFitLow),
                      self.rules.ldlRule.ldlFitHigh), self.rules.hdlRule.hdlFitHigh), self.rules.riskRule.riskMid)
        self.rule4 = fmin(
            fmin(fmin(fmin(self.rules.bloodRule.bloodPressureFitLow, self.rules.cholesterolRule.cholesterolFitLow),
                      self.rules.ldlRule.ldlFitVeryHigh), self.rules.hdlRule.hdlFitHigh),
            self.rules.riskRule.riskHigh)
        self.rule5 = fmin(fmin(fmin(self.rules.bloodRule.bloodPressureFitMid, self.rules.cholesterolRule.cholesterolFitLow),
                               self.rules.hdlRule.hdlFitHigh), self.rules.riskRule.riskNot)

        self.rule6 = fmin(fmin(fmin(self.rules.ageRule.ageFitYoung, self.rules.bloodRule.bloodPressureFitMid),
                               self.rules.cholesterolRule.cholesterolFitMid), self.rules.riskRule.riskNot)
        self.rule7 = fmin(fmin(fmin(self.rules.ageRule.ageFitMid, self.rules.bloodRule.bloodPressureFitMid),
                               self.rules.cholesterolRule.cholesterolFitMid), self.rules.riskRule.riskNot)
        self.rule8 = fmin(fmin(fmin(self.rules.ageRule.ageFitOld, self.rules.bloodRule.bloodPressureFitMid),
                               self.rules.cholesterolRule.cholesterolFitMid), self.rules.riskRule.riskNot)
        self.rule9 = fmin(fmin(fmin(self.rules.ageRule.ageFitYoung, self.rules.cholesterolRule.cholesterolFitHigh),
                               self.rules.cholesterolRule.cholesterolFitHigh), self.rules.riskRule.riskMid)
        self.rule10 = fmin(fmin(fmin(self.rules.ageRule.ageFitMid, self.rules.cholesterolRule.cholesterolFitHigh),
                                self.rules.cholesterolRule.cholesterolFitHigh), self.rules.riskRule.riskHigh)

        self.rule11 = fmin(fmin(fmin(self.rules.ageRule.ageFitOld, self.rules.bloodRule.bloodPressureFitHigh),
                                self.rules.cholesterolRule.cholesterolFitHigh), self.rules.riskRule.riskVeryHigh)

        self.rule12 = fmin(fmin(fmin(fmin(fmin(self.rules.ageRule.ageFitYoung, self.rules.bloodRule.bloodPressureFitMid),
                                          self.rules.cholesterolRule.cholesterolFitLow), self.rules.ldlRule.ldlFitNormal),
                                self.rules.hdlRule.hdlFitLow), self.rules.riskRule.riskNot)
        self.rule13 = fmin(fmin(self.rules.ageRule.ageFitYoung, self.rules.bloodSugarRule.bloodSugarFitVeryHigh),
                           self.rules.riskRule.riskLittle)
        self.rule14 = fmin(fmin(self.rules.ageRule.ageFitMid, self.rules.bloodSugarRule.bloodSugarFitVeryHigh),
                           self.rules.riskRule.riskHigh)
        self.rule15 = fmin(fmin(self.rules.ageRule.ageFitOld, self.rules.bloodSugarRule.bloodSugarFitVeryHigh),
                           self.rules.riskRule.riskVeryHigh)
        self.rule16 = fmin(fmin(fmin(fmin(fmin(fmin(self.rules.ageRule.ageFitYoung,
                                                    self.rules.bloodRule.bloodPressureFitLow),
                                               self.rules.cholesterolRule.cholesterolFitLow),
                                          self.rules.bloodSugarRule.bloodSugarFitVeryHigh), self.rules.ldlRule.ldlFitNormal),
                                self.rules.hdlRule.hdlFitHigh),
                           self.rules.riskRule.riskLittle)
        self.rule17 = fmin(fmin(fmin(fmin(fmin(fmin(self.rules.ageRule.ageFitMid, self.rules.bloodRule.bloodPressureFitLow),
                                               self.rules.cholesterolRule.cholesterolFitLow),
                                          self.rules.bloodSugarRule.bloodSugarFitVeryHigh), self.rules.ldlRule.ldlFitNormal),
                                self.rules.hdlRule.hdlFitHigh), self.rules.riskRule.riskHigh)
        self.rule18 = fmin(fmin(fmin(fmin(fmin(fmin(self.rules.ageRule.ageFitOld, self.rules.bloodRule.bloodPressureFitLow),
                                               self.rules.cholesterolRule.cholesterolFitLow),
                                          self.rules.bloodSugarRule.bloodSugarFitVeryHigh), self.rules.ldlRule.ldlFitNormal),
                                self.rules.hdlRule.hdlFitHigh), self.rules.riskRule.riskVeryHigh)
        self.rule19 = fmin(fmin(fmin(fmin(fmin(fmin(self.rules.ageRule.ageFitMid, self.rules.bloodRule.bloodPressureFitLow),
                                               self.rules.cholesterolRule.cholesterolFitLow),
                                          self.rules.bloodSugarRule.bloodSugarFitVeryHigh), self.rules.ldlRule.ldlFitVeryHigh),
                                self.rules.hdlRule.hdlFitHigh), self.rules.riskRule.riskVeryHigh)

        self.rule20 = fmin(fmin(
            fmin(fmin(self.rules.bloodRule.bloodPressureFitHigh, self.rules.cholesterolRule.cholesterolFitHigh),
                 self.rules.ldlRule.ldlFitVeryHigh), self.rules.hdlRule.hdlFitHigh), self.rules.riskRule.riskVeryHigh)
        self.rule21 = fmin(fmin(
            fmin(fmin(self.rules.cholesterolRule.cholesterolFitHigh, self.rules.cholesterolRule.cholesterolFitHigh),
                 self.rules.ldlRule.ldlFitHigh), self.rules.hdlRule.hdlFitMid), self.rules.riskRule.riskVeryHigh)
        self.rule22 = fmin(fmin(fmin(fmin(fmin(self.rules.ageRule.ageFitYoung, self.rules.bloodRule.bloodPressureFitHigh),
                                          self.rules.cholesterolRule.cholesterolFitHigh), self.rules.ldlRule.ldlFitVeryHigh),
                                self.rules.hdlRule.hdlFitMid), self.rules.riskRule.riskMid)
        self.rule23 = fmin(fmin(self.rules.ageRule.ageFitMid, self.rules.bloodRule.bloodPressureFitHigh),
                           self.rules.riskRule.riskVeryHigh)
        self.rule24 = fmin(fmin(self.rules.ageRule.ageFitOld, self.rules.bloodRule.bloodPressureFitHigh),
                           self.rules.riskRule.riskVeryHigh)


    def cloudyInferenceEngine(self):
        # Union sets
        self.uninfected = fmax(fmax(fmax(fmax(fmax(self.rule1, self.rule5), self.rule6), self.rule7), self.rule8), self.rule12)
        self.little = fmax(fmax(self.rule2, self.rule13), self.rule16)
        self.mid = fmax(fmax(self.rule3, self.rule9), self.rule22)
        self.high = fmax(fmax(fmax(self.rule4, self.rule10), self.rule14), self.rule17)
        self.veryHigh = fmax(
            fmax(fmax(fmax(fmax(fmax(fmax(self.rule11, self.rule15), self.rule18), self.rule19), self.rule20), self.rule21), self.rule23), self.rule24)