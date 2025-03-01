import json
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# OWASP Risk Rating Factors
LIKELIHOOD_FACTORS = {
    "threat_agent": {"Anonymous": 1, "Insider": 2, "Advanced Persistent Threat (APT)": 3},
    "vulnerability": {"Low": 1, "Medium": 2, "High": 3},
}

IMPACT_FACTORS = {
    "technical": {"Low": 1, "Medium": 2, "High": 3},
    "business": {"Minimal": 1, "Significant": 2, "Severe": 3},
}

# OWASP Risk Calculation
def calculate_owasp_risk(threat_agent, vulnerability, technical, business):
    likelihood = LIKELIHOOD_FACTORS["threat_agent"][threat_agent] * LIKELIHOOD_FACTORS["vulnerability"][vulnerability]
    impact = IMPACT_FACTORS["technical"][technical] * IMPACT_FACTORS["business"][business]
    risk = likelihood * impact

    # Determine Risk Level
    if risk <= 4:
        risk_level = "Low"
    elif 5 <= risk <= 9:
        risk_level = "Medium"
    else:
        risk_level = "High"

    return {"Likelihood": likelihood, "Impact": impact, "Risk Score": risk, "Risk Level": risk_level}

# Function to save results to JSON
def save_risk_report(data, filename="owasp_risk_report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

# GUI Interface for OWASP Risk Calculator
def run_gui():
    def calculate():
        threat_agent = threat_agent_var.get()
        vulnerability = vulnerability_var.get()
        technical = technical_var.get()
        business = business_var.get()

        result = calculate_owasp_risk(threat_agent, vulnerability, technical, business)
        
        messagebox.showinfo("OWASP Risk Assessment", f"Risk Level: {result['Risk Level']}\nRisk Score: {result['Risk Score']}")
        save_risk_report(result)

        visualize_risk(result)

    # GUI Window
    root = tk.Tk()
    root.title("OWASP Risk Calculator")

    tk.Label(root, text="Select Threat Agent:").grid(row=0, column=0)
    threat_agent_var = tk.StringVar(root)
    tk.OptionMenu(root, threat_agent_var, *LIKELIHOOD_FACTORS["threat_agent"]).grid(row=0, column=1)

    tk.Label(root, text="Select Vulnerability Level:").grid(row=1, column=0)
    vulnerability_var = tk.StringVar(root)
    tk.OptionMenu(root, vulnerability_var, *LIKELIHOOD_FACTORS["vulnerability"]).grid(row=1, column=1)

    tk.Label(root, text="Select Technical Impact:").grid(row=2, column=0)
    technical_var = tk.StringVar(root)
    tk.OptionMenu(root, technical_var, *IMPACT_FACTORS["technical"]).grid(row=2, column=1)

    tk.Label(root, text="Select Business Impact:").grid(row=3, column=0)
    business_var = tk.StringVar(root)
    tk.OptionMenu(root, business_var, *IMPACT_FACTORS["business"]).grid(row=3, column=1)

    tk.Button(root, text="Calculate Risk", command=calculate).grid(row=4, column=0, columnspan=2)
    
    root.mainloop()

# Visualization Function
def visualize_risk(risk_data):
    labels = ["Likelihood", "Impact", "Risk Score"]
    values = [risk_data["Likelihood"], risk_data["Impact"], risk_data["Risk Score"]]

    plt.bar(labels, values, color=["blue", "orange", "red"])
    plt.title(f"OWASP Risk Score - {risk_data['Risk Level']}")
    plt.xlabel("Factors")
    plt.ylabel("Score")
    plt.savefig("owasp_risk_chart.png")
    plt.show()

# Run GUI if script is executed
if __name__ == "__main__":
    run_gui()
