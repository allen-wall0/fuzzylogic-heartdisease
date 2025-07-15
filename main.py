# main.py (No Changes - provided for completeness)
import tkinter as tk
from HeartDiagnosis import HeartDiagnosisGUI # Import the new GUI class

if "__main__" == __name__:
    root = tk.Tk()
    app = HeartDiagnosisGUI(root)
    root.mainloop()