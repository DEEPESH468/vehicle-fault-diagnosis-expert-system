# 🚗 Vehicle Fault Diagnostic Expert System

A **Rule-Based Expert System** developed as part of my **PBL (Project-Based Learning)** assignment.  
This system diagnoses common vehicle faults based on user-described symptoms using simple **IF–THEN rules**, similar to how a mechanic uses experience to identify issues.

---

## 📌 Project Overview

This project demonstrates how **Expert Systems** can be used to simulate decision-making capabilities of human experts.  
The system takes **symptoms as text input** and predicts **possible faults** in the vehicle.

The goal is to:
- Provide a simple automated diagnostic tool  
- Reduce dependency on initial manual inspection  
- Showcase the use of Rule-Based AI in real-world domains  

---

## 🧠 How the System Works

The system uses **Rule-Based Reasoning**, where each rule follows the structure:


When the user describes symptoms, the program matches keywords like:
- knocking  
- burning smell  
- vibration  
- brake  
- temperature high  
- check engine light  

Based on the match, it displays the most likely cause.

---

## 🧪 Features

✔ Rule-Based Expert System  
✔ Simple & beginner-friendly  
✔ Real-world vehicle issues covered  
✔ User-friendly text input  
✔ Expandable with more rules  

---

## 🛠 Technologies Used

- **Python (Core Programming Language)**
- **Rule-Based Expert System Logic**

---

## 🧩 Code Snippet

```python
# Vehicle Fault Diagnosis Expert System
# Rule-Based System using simple IF-THEN rules

def diagnose_vehicle(symptoms):
    symptoms = symptoms.lower()

    # Rule 1: Engine Knocking Sound
    if "knocking" in symptoms or "tapping" in symptoms:
        return "Possible Fault: Low Engine Oil or Faulty Spark Plugs."

    # Rule 2: Burning Smell
    elif "burning smell" in symptoms or "smoke" in symptoms:
        return "Possible Fault: Overheating, Oil Leakage, or Clutch Burning."

    # Rule 3: Check Engine Light
    elif "check engine light" in symptoms or "engine light" in symptoms:
        return "Possible Fault: Engine Misfire, Sensor Failure, or Fuel System Issue."

    # Rule 4: Clicking Sound while Starting
    elif "clicking sound" in symptoms or "does not start" in symptoms:
        return "Possible Fault: Weak Battery or Faulty Starter Motor."

    # Rule 5: Vibrations while Driving
    elif "vibration" in symptoms or "shaking" in symptoms:
        return "Possible Fault: Wheel Misalignment or Tire Damage."

    # Rule 6: Brake Warning Light / Squealing Sound
    elif "brake" in symptoms or "squealing sound" in symptoms:
        return "Possible Fault: Worn Brake Pads or Brake Fluid Leakage."

    # Rule 7: Overheating Issue
    elif "overheat" in symptoms or "temperature high" in symptoms:
        return "Possible Fault: Coolant Leak or Radiator Problem."

    else:
        return "Fault Unknown: Please provide more symptoms or visit a mechanic."


