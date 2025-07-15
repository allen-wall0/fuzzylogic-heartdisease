import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from numpy import zeros_like, fmax
import skfuzzy as fuzz

# Import the universe of discourse variables directly from Configurations
from Configurations import (
    age, bloodPressure, cholesterol, bloodSugar,
    highDensityLipoprotein, lowDensityLipoprotein, risk
)

# Import all RuleBase classes
from RuleBase.Age import Age
from RuleBase.BloodPressure import BloodPressure
from RuleBase.Cholesterol import Cholesterol
from RuleBase.BloodSugar import BloodSugar
from RuleBase.LowDensityLipoprotein import LowDensityLipoprotein
from RuleBase.HighDensityLipoprotein import HighDensityLipoprotein
from RuleBase.RiskRule import RiskRule
from Risk import Risk

# Define ranges for GUI labels (these are just for display in the GUI, not used in fuzzy logic calculations directly)
AGE_RANGE = (0, 100)
BP_RANGE = (0, 220)
CHOLESTEROL_RANGE = (100, 250)
BS_RANGE = (0, 120)
LDL_RANGE = (0, 190)
HDL_RANGE = (0, 70)
RISK_OUTPUT_RANGE = (0, 45) # Max risk score from configurations is 45

class HeartDiagnosisGUI:
    def __init__(self, master):
        self.master = master
        master.title("Heart Disease Risk Calculation")
        master.geometry("400x550")

        self.userAge = None
        self.userBloodPressure = None
        self.userCholesterol = None
        self.userBloodSugar = None
        self.userLDL = None
        self.userHDL = None

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Heart Disease Diagnosis", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.master, text="Enter health data for Heart Disease Risk Calculation").pack()

        # Age Input
        tk.Label(self.master, text=f"Enter Age (years): Range {AGE_RANGE[0]}-{AGE_RANGE[1]}").pack(pady=5)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.pack()

        # Blood Pressure Input
        tk.Label(self.master, text=f"Enter Blood Pressure (mmHg): Range {BP_RANGE[0]}-{BP_RANGE[1]}").pack(pady=5)
        self.bp_entry = tk.Entry(self.master)
        self.bp_entry.pack()

        # Cholesterol Input
        tk.Label(self.master, text=f"Enter Cholesterol (mg/dL): Range {CHOLESTEROL_RANGE[0]}-{CHOLESTEROL_RANGE[1]}").pack(pady=5)
        self.cholesterol_entry = tk.Entry(self.master)
        self.cholesterol_entry.pack()

        # Blood Sugar Input
        tk.Label(self.master, text=f"Enter Blood Sugar (mg/dL): Range {BS_RANGE[0]}-{BS_RANGE[1]}").pack(pady=5)
        self.bs_entry = tk.Entry(self.master)
        self.bs_entry.pack()

        # LDL Input
        tk.Label(self.master, text=f"Enter Low Density Lipoprotein (mg/dL): Range {LDL_RANGE[0]}-{LDL_RANGE[1]}").pack(pady=5)
        self.ldl_entry = tk.Entry(self.master)
        self.ldl_entry.pack()

        # HDL Input
        tk.Label(self.master, text=f"Enter High Density Lipoprotein (mg/dL): Range {HDL_RANGE[0]}-{HDL_RANGE[1]}").pack(pady=5)
        self.hdl_entry = tk.Entry(self.master)
        self.hdl_entry.pack()

        self.calculate_button = tk.Button(self.master, text="Calculate Risk", command=self.process_input)
        self.calculate_button.pack(pady=20)

        self.result_label = tk.Label(self.master, text="Coroner Heart Diagnosis: ", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def validate_input(self, entry_widget, min_val, max_val, field_name):
        try:
            value = int(entry_widget.get())
            if not (min_val <= value <= max_val):
                messagebox.showerror("Input Error", f"{field_name} must be between {min_val} and {max_val}.")
                return None
            return value
        except ValueError:
            messagebox.showerror("Input Error", f"Please enter a valid integer for {field_name}.")
            return None

    def process_input(self):
        self.userAge = self.validate_input(self.age_entry, *AGE_RANGE, "Age")
        self.userBloodPressure = self.validate_input(self.bp_entry, *BP_RANGE, "Blood Pressure")
        self.userCholesterol = self.validate_input(self.cholesterol_entry, *CHOLESTEROL_RANGE, "Cholesterol")
        self.userBloodSugar = self.validate_input(self.bs_entry, *BS_RANGE, "Blood Sugar")
        self.userLDL = self.validate_input(self.ldl_entry, *LDL_RANGE, "Low Density Lipoprotein")
        self.userHDL = self.validate_input(self.hdl_entry, *HDL_RANGE, "High Density Lipoprotein")

        if all(val is not None for val in [self.userAge, self.userBloodPressure, self.userCholesterol,
                                           self.userBloodSugar, self.userLDL, self.userHDL]):
            self.heartDiagnosis()
        else:
            self.result_label.config(text="Please correct input errors.")

    def heartDiagnosis(self):
        # Initialize and fuzzify Age
        ageRule = Age()
        ageRule.trapezoidalMembership() # Uses trapezoidal membership
        ageRule.membershipDegrees(self.userAge)

        # Initialize and fuzzify Blood Pressure
        bloodRule = BloodPressure()
        bloodRule.trapezoidalMembership() # Uses trapezoidal membership
        bloodRule.membershipDegrees(self.userBloodPressure)

        # Initialize and fuzzify Cholesterol
        cholesterolRule = Cholesterol()
        cholesterolRule.trapezoidalMembership() # Uses trapezoidal membership
        cholesterolRule.membershipDegrees(self.userCholesterol)

        # Initialize and fuzzify Blood Sugar
        bloodSugarRule = BloodSugar()
        bloodSugarRule.triangularMembership() # Calls triangular membership
        bloodSugarRule.membershipDegrees(self.userBloodSugar)

        # Initialize and fuzzify Low Density Lipoprotein
        ldlRule = LowDensityLipoprotein()
        ldlRule.triangularMembership() # Calls triangular membership
        ldlRule.membershipDegrees(self.userLDL)

        # Initialize and fuzzify High Density Lipoprotein
        hdlRule = HighDensityLipoprotein()
        hdlRule.triangularMembership() # Calls triangular membership
        hdlRule.membershipDegrees(self.userHDL)

        # Initialize Risk Rule
        riskRule = RiskRule()
        riskRule.trapezoidalMembership() # Uses trapezoidal membership

        riskValues = Risk(ageRule=ageRule,
                          bloodRule=bloodRule,
                          cholesterolRule=cholesterolRule,
                          bloodSugarRule=bloodSugarRule,
                          ldlRule=ldlRule,
                          hdlRule=hdlRule,
                          riskRule=riskRule)

        riskValues.inferenceSystems()
        riskValues.cloudyInferenceEngine()

        # Defuzzification
        crispValue = fmax(fmax(fmax(fmax(riskValues.uninfected, riskValues.little), riskValues.mid), riskValues.high), riskValues.veryHigh)
        defuzzified = fuzz.defuzz(risk, crispValue, "mom")
        result_membership = fuzz.interp_membership(risk, crispValue, defuzzified)

        # Update GUI label with the result
        self.result_label.config(text=f"Coroner Heart Diagnosis: {defuzzified:.2f}")

        # Close any existing matplotlib windows to prevent accumulation
        plt.close('all')

        # Create a single figure with multiple subplots for better organization
        fig, axes = plt.subplots(3, 3, figsize=(15, 12))
        fig.suptitle('Heart Disease Risk Assessment - Fuzzy Logic Analysis', fontsize=16, fontweight='bold')

        # Age Membership Function Plot
        axes[0, 0].plot(age, ageRule.ageYoung, 'b', linewidth=1.5, label='Young')
        axes[0, 0].plot(age, ageRule.ageMid, 'g', linewidth=1.5, label='Mid')
        axes[0, 0].plot(age, ageRule.ageOld, 'r', linewidth=1.5, label='Old')
        axes[0, 0].axvline(x=self.userAge, color='k', linestyle='--', alpha=0.7, label=f'Input: {self.userAge}')
        axes[0, 0].set_title('Age Rule Membership Function')
        axes[0, 0].set_ylabel('Membership degree')
        axes[0, 0].set_xlabel('Age (years)')
        axes[0, 0].legend()
        axes[0, 0].grid(True, alpha=0.3)

        # Blood Pressure Membership Function Plot
        axes[0, 1].plot(bloodPressure, bloodRule.bloodPressureLow, 'b', linewidth=1.5, label='Low')
        axes[0, 1].plot(bloodPressure, bloodRule.bloodPressureMid, 'g', linewidth=1.5, label='Mid')
        axes[0, 1].plot(bloodPressure, bloodRule.bloodPressureHigh, 'r', linewidth=1.5, label='High')
        axes[0, 1].plot(bloodPressure, bloodRule.bloodPressureVeryHigh, 'orange', linewidth=1.5, label='Very High')
        axes[0, 1].axvline(x=self.userBloodPressure, color='k', linestyle='--', alpha=0.7, label=f'Input: {self.userBloodPressure}')
        axes[0, 1].set_title('Blood Pressure Rule Membership Function')
        axes[0, 1].set_ylabel('Membership degree')
        axes[0, 1].set_xlabel('Blood Pressure (mmHg)')
        axes[0, 1].legend()
        axes[0, 1].grid(True, alpha=0.3)

        # Cholesterol Membership Function Plot
        axes[0, 2].plot(cholesterol, cholesterolRule.cholesterolLow, 'b', linewidth=1.5, label='Low')
        axes[0, 2].plot(cholesterol, cholesterolRule.cholesterolMid, 'g', linewidth=1.5, label='Mid')
        axes[0, 2].plot(cholesterol, cholesterolRule.cholesterolHigh, 'r', linewidth=1.5, label='High')
        axes[0, 2].axvline(x=self.userCholesterol, color='k', linestyle='--', alpha=0.7, label=f'Input: {self.userCholesterol}')
        axes[0, 2].set_title('Cholesterol Rule Membership Function')
        axes[0, 2].set_ylabel('Membership degree')
        axes[0, 2].set_xlabel('Cholesterol (mg/dL)')
        axes[0, 2].legend()
        axes[0, 2].grid(True, alpha=0.3)

        # Blood Sugar Membership Function Plot
        axes[1, 0].plot(bloodSugar, bloodSugarRule.bloodSugarVeryHigh, 'm', linewidth=1.5, label='Very High')
        axes[1, 0].axvline(x=self.userBloodSugar, color='k', linestyle='--', alpha=0.7, label=f'Input: {self.userBloodSugar}')
        axes[1, 0].set_title('Blood Sugar Rule Membership Function')
        axes[1, 0].set_ylabel('Membership degree')
        axes[1, 0].set_xlabel('Blood Sugar (mg/dL)')
        axes[1, 0].legend()
        axes[1, 0].grid(True, alpha=0.3)

        # Low Density Lipoprotein Membership Function Plot
        axes[1, 1].plot(lowDensityLipoprotein, ldlRule.ldlNormal, 'b', linewidth=1.5, label='Normal')
        axes[1, 1].plot(lowDensityLipoprotein, ldlRule.ldlLimit, 'g', linewidth=1.5, label='Limit')
        axes[1, 1].plot(lowDensityLipoprotein, ldlRule.ldlHigh, 'r', linewidth=1.5, label='High')
        axes[1, 1].plot(lowDensityLipoprotein, ldlRule.ldlVeryHigh, 'm', linewidth=1.5, label='Very High')
        axes[1, 1].axvline(x=self.userLDL, color='k', linestyle='--', alpha=0.7, label=f'Input: {self.userLDL}')
        axes[1, 1].set_title('LDL Rule Membership Function')
        axes[1, 1].set_ylabel('Membership degree')
        axes[1, 1].set_xlabel('LDL (mg/dL)')
        axes[1, 1].legend()
        axes[1, 1].grid(True, alpha=0.3)

        # High Density Lipoprotein Membership Function Plot
        axes[1, 2].plot(highDensityLipoprotein, hdlRule.hdlLow, 'b', linewidth=1.5, label='Low')
        axes[1, 2].plot(highDensityLipoprotein, hdlRule.hdlMid, 'g', linewidth=1.5, label='Mid')
        axes[1, 2].plot(highDensityLipoprotein, hdlRule.hdlHigh, 'r', linewidth=1.5, label='High')
        axes[1, 2].axvline(x=self.userHDL, color='k', linestyle='--', alpha=0.7, label=f'Input: {self.userHDL}')
        axes[1, 2].set_title('HDL Rule Membership Function')
        axes[1, 2].set_ylabel('Membership degree')
        axes[1, 2].set_xlabel('HDL (mg/dL)')
        axes[1, 2].legend()
        axes[1, 2].grid(True, alpha=0.3)

        # Risk Rule Membership Functions
        axes[2, 0].plot(risk, riskRule.riskNot, 'b', linewidth=1.5, label='Not Infected')
        axes[2, 0].plot(risk, riskRule.riskLittle, 'g', linewidth=1.5, label='Little Risk')
        axes[2, 0].plot(risk, riskRule.riskMid, 'orange', linewidth=1.5, label='Mid Risk')
        axes[2, 0].plot(risk, riskRule.riskHigh, 'r', linewidth=1.5, label='High Risk')
        axes[2, 0].plot(risk, riskRule.riskVeryHigh, 'm', linewidth=1.5, label='Very High Risk')
        axes[2, 0].set_title('Risk Rule Membership Functions')
        axes[2, 0].set_ylabel('Membership degree')
        axes[2, 0].set_xlabel('Risk Score')
        axes[2, 0].legend()
        axes[2, 0].grid(True, alpha=0.3)

        # Combined Risk Output with Defuzzification
        risk0 = zeros_like(risk)
        axes[2, 1].plot(risk, riskRule.riskNot, 'b', linewidth=0.5, linestyle="--", alpha=0.7)
        axes[2, 1].plot(risk, riskRule.riskLittle, 'g', linewidth=0.5, linestyle="--", alpha=0.7)
        axes[2, 1].plot(risk, riskRule.riskMid, 'orange', linewidth=0.5, linestyle="--", alpha=0.7)
        axes[2, 1].plot(risk, riskRule.riskHigh, 'r', linewidth=0.5, linestyle="--", alpha=0.7)
        axes[2, 1].plot(risk, riskRule.riskVeryHigh, 'm', linewidth=0.5, linestyle="--", alpha=0.7)
        axes[2, 1].fill_between(risk, risk0, crispValue, facecolor="Orange", alpha=0.7, label='Combined Output')
        axes[2, 1].axvline(x=defuzzified, color='k', linewidth=2, alpha=0.9, label=f'Defuzzified: {defuzzified:.2f}')
        axes[2, 1].set_title("Combined Risk Output & Defuzzification")
        axes[2, 1].set_ylabel('Membership degree')
        axes[2, 1].set_xlabel('Risk Score')
        axes[2, 1].legend()
        axes[2, 1].grid(True, alpha=0.3)

        # Risk Interpretation
        axes[2, 2].axis('off')
        risk_interpretation = self.get_risk_interpretation(defuzzified)
        axes[2, 2].text(0.1, 0.7, f"Risk Score: {defuzzified:.2f}", fontsize=14, fontweight='bold', 
                       transform=axes[2, 2].transAxes)
        axes[2, 2].text(0.1, 0.5, f"Risk Level: {risk_interpretation['level']}", fontsize=12, 
                       transform=axes[2, 2].transAxes, color=risk_interpretation['color'])
        axes[2, 2].text(0.1, 0.3, f"Recommendation:", fontsize=12, fontweight='bold', 
                       transform=axes[2, 2].transAxes)
        axes[2, 2].text(0.1, 0.1, risk_interpretation['recommendation'], fontsize=10, 
                       transform=axes[2, 2].transAxes, wrap=True)
        axes[2, 2].set_title("Risk Assessment Summary")

        plt.tight_layout()
        plt.show()

    def get_risk_interpretation(self, risk_score):
        """Provide interpretation of the risk score"""
        if risk_score <= 10:
            return {
                'level': 'Very Low Risk',
                'color': 'green',
                'recommendation': 'Maintain current lifestyle. Regular check-ups recommended.'
            }
        elif risk_score <= 20:
            return {
                'level': 'Low Risk',
                'color': 'lightgreen',
                'recommendation': 'Good health status. Continue healthy habits.'
            }
        elif risk_score <= 30:
            return {
                'level': 'Moderate Risk',
                'color': 'orange',
                'recommendation': 'Consider lifestyle improvements. Consult healthcare provider.'
            }
        elif risk_score <= 40:
            return {
                'level': 'High Risk',
                'color': 'red',
                'recommendation': 'Immediate medical attention recommended. Lifestyle changes needed.'
            }
        else:
            return {
                'level': 'Very High Risk',
                'color': 'darkred',
                'recommendation': 'Urgent medical attention required. Comprehensive treatment needed.'
            }

# This part is for the GUI, and replaces your original text-based HeartDiagnosis entry point
if __name__ == '__main__':
    root = tk.Tk()
    app = HeartDiagnosisGUI(root)
    root.mainloop()
