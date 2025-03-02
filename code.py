import json, matplotlib.pyplot as plt, tkinter as tk
from tkinter import messagebox

# Some random risk values 
risk_values = {
    "thrt": {"Anon": 1, "Insdr": 2, "APT": 3},  # idk why these are diff but okay
    "vuln": {"Lo": 1, "Med": 2, "Hi": 3},
}

impact_values = {
    "tech": {"Lo": 1, "Med": 2, "Hi": 3},
    "biz": {"Min": 1, "Sig": 2, "Sev": 3},
}

# Debug mode (set True for debugging)
debug = False  

# Calculate risk (probably works?)
def doRiskStuff(th, v, t, b):
    try:
        like = risk_values["thrt"][th] * risk_values["vuln"][v]
        imp = impact_values["tech"][t] * impact_values["biz"][b]
        score = like * imp

        # Assigning risk level (feels arbitrary tbh)
        lvl = "Lo"
        if 5 <= score <= 9:
            lvl = "Med"
        elif score > 9:
            lvl = "Hi"

        return {"Likelihood": like, "Impact": imp, "Risk Score": score, "Risk Level": lvl}
    
    except KeyError:
        return {"error": "Invalid input values!"}  # Prevent crashes if something is missing

# Save JSON report (why not)
def dumpRiskToJson(x, f="owasp_risk_report.json"):
    with open(f, "w") as o:
        json.dump(x, o, indent=4)

# Make a window thing (GUI??)
def startWindow():
    def calcBtnClick():
        t = t_var.get()
        v = v_var.get()
        te = te_var.get()
        b = b_var.get()

        # Check if all options are selected
        if not t or not v or not te or not b:
            messagebox.showerror("Error", "Please select all values!")
            return

        r = doRiskStuff(t, v, te, b)

        if "error" in r:
            messagebox.showerror("Error", r["error"])
            return
        
        messagebox.showinfo("OWASP Risk Assessment", f"Risk Level: {r['Risk Level']}\nRisk Score: {r['Risk Score']}")
        dumpRiskToJson(r)

        if debug:
            print(f"DEBUG: {r}")

        drawGraph(r)  # Oh yeah, forgot about this part

    w = tk.Tk()
    w.title("Risk Calc Window")

    tk.Label(w, text="Threat Type:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
    t_var = tk.StringVar(w)
    t_var.set("Anon")  # Set a default value
    tk.OptionMenu(w, t_var, *risk_values["thrt"]).grid(row=0, column=1, padx=5, pady=2)

    tk.Label(w, text="Vuln Level:").grid(row=1, column=0, sticky="w", padx=5, pady=2)
    v_var = tk.StringVar(w)
    v_var.set("Lo")  # Set a default value
    tk.OptionMenu(w, v_var, *risk_values["vuln"]).grid(row=1, column=1, padx=5, pady=2)

    tk.Label(w, text="Tech Impact:").grid(row=2, column=0, sticky="w", padx=5, pady=2)
    te_var = tk.StringVar(w)
    te_var.set("Lo")  # Set a default value
    tk.OptionMenu(w, te_var, *impact_values["tech"]).grid(row=2, column=1, padx=5, pady=2)

    tk.Label(w, text="Biz Impact:").grid(row=3, column=0, sticky="w", padx=5, pady=2)
    b_var = tk.StringVar(w)
    b_var.set("Min")  # Set a default value
    tk.OptionMenu(w, b_var, *impact_values["biz"]).grid(row=3, column=1, padx=5, pady=2)

    tk.Button(w, text="Go", command=calcBtnClick).grid(row=4, column=0, columnspan=2, pady=10)
    
    w.mainloop()

# Draw graph thing
def drawGraph(r):
    labels = ["Likelihood", "Impact", "Risk Score"]
    values = [r["Likelihood"], r["Impact"], r["Risk Score"]]

    plt.bar(labels, values, color=["blue", "orange", "red"])
    plt.title(f"Risk Level: {r['Risk Level']}")
    plt.xlabel("Stuff")
    plt.ylabel("Nums")
    plt.savefig("owasp_risk_chart.png")  # Saving this bc why not
    plt.show()

# Run it 
if __name__ == "__main__":
    startWindow()
