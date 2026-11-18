# Medical Diagnosis System

# Function to diagnose disease
def diagnosis(symptoms):

    if "fever" in symptoms and "cough" in symptoms:
        return "Possible Flu"

    elif "fever" in symptoms and "headache" in symptoms:
        return "Possible Viral Infection"

    elif "sneezing" in symptoms and "runny nose" in symptoms:
        return "Possible Common Cold"

    elif "headache" in symptoms and "nausea" in symptoms:
        return "Possible Migraine"

    elif "stomach pain" in symptoms and "vomiting" in symptoms:
        return "Possible Stomach Infection"

    else:
        return "Diagnosis not available"


# Main Program
print("MEDICAL DIAGNOSIS SYSTEM")
print("------------------------")

print("Enter symptoms separated by commas")

user_input = input("Enter Symptoms: ")

symptoms = [s.strip().lower() for s in user_input.split(",")]

result = diagnosis(symptoms)

print("\nDiagnosis Result:")
print(result)
