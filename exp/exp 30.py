# Backward Chaining Algorithm

# Initial Facts
facts = {
    "fever",
    "cough"
}

# Rules: Conditions -> Conclusion
rules = {
    "flu": ["fever", "cough"],
    "take_rest": ["flu"],
    "consult_doctor": ["flu"],
    "high_temperature": ["fever"],
    "possible_infection": ["cough", "high_temperature"]
}


# Backward Chaining Function
def backward_chaining(goal):

    # Check whether goal is a known fact
    if goal in facts:
        return True

    # Check whether goal can be derived using rules
    if goal in rules:

        for condition in rules[goal]:

            if not backward_chaining(condition):
                return False

        return True

    return False


# Main Program
print("BACKWARD CHAINING SYSTEM")
print("------------------------")

query = input("Enter the goal to check: ").lower()

if backward_chaining(query):
    print("\nGoal", query, "is TRUE")
else:
    print("\nGoal", query, "is FALSE")
