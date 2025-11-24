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


# Main Program
print("=== Vehicle Fault Diagnosis Expert System ===")
user_symptoms = input("Describe the symptoms you are noticing in your vehicle: ")

result = diagnose_vehicle(user_symptoms)
print("\nDiagnosis:")
print(result)
