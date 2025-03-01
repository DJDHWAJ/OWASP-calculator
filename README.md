# OWASP Risk Calculator

## **Objective**
The goal of this project is to implement an **OWASP Risk Calculator** that provides a structured approach to evaluating security risks based on the **OWASP Risk Rating Methodology**. This tool allows cybersecurity professionals, developers, and security analysts to assess vulnerabilities efficiently and determine risk levels based on **likelihood** and **impact** factors.

## **What is the OWASP Risk Rating Methodology?**
The **OWASP Risk Rating Model** is a standardized framework for assessing cybersecurity risks by evaluating **Likelihood** (how likely a vulnerability will be exploited) and **Impact** (the damage caused if it is exploited). The risk score is calculated using the formula:

```
Risk Score = Likelihood × Impact
```

Each factor is broken down as follows:
- **Likelihood Factors**
  - **Threat Agent** (Skill level, motive, opportunity, size)
  - **Vulnerability Factors** (Ease of discovery, exploitability, awareness, intrusion detection)

- **Impact Factors**
  - **Technical Impact** (Loss of confidentiality, integrity, availability, accountability)
  - **Business Impact** (Loss of revenue, reputation damage, compliance issues)

The final risk score determines the **Risk Level**:
- **Low Risk (1 - 4)**: Minimal impact, difficult to exploit.
- **Medium Risk (5 - 9)**: Moderate impact, can be exploited.
- **High Risk (10 - 25)**: Severe impact, highly exploitable.

Example Output

Risk Assessment Report

The calculated risk assessment is saved in outputs/owasp_risk_report.json. Example:
```json
{
    "Likelihood": 3,
    "Impact": 9,
    "Risk Score": 27,
    "Risk Level": "High"
}
```

Risk Visualization

The risk level is also visualized as a bar chart: ![OWASP Risk Chart](https://github.com/DJDHWAJ/OWASP-calculator/blob/main/owasp_risk_chart.png)
## **Project Outcome**
By using this OWASP Risk Calculator, security teams can:
✅ **Quantify security risks consistently** using OWASP’s structured methodology.  
✅ **Make data-driven security decisions** based on calculated risk levels.  
✅ **Generate risk reports** for documentation and compliance audits.  
✅ **Visualize risk factors** to enhance risk assessment presentations.  

## **Features**
- **Automated OWASP Risk Calculation**
- **Graphical Representation of Risks**
- **Custom User Input for Risk Evaluation** 
- **JSON Report Generation**






## **Next Steps**
- **Enhance model with machine learning-based risk prediction**.
- **Expand OWASP factor customization for more flexibility**.
- **Integrate with SIEM tools for real-time risk monitoring**.

This project provides a structured and automated approach to risk assessment, making security evaluations faster and more reliable. 









