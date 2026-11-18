# Forward Chaining Algorithm

# Initial Facts
facts = {
    "fever",
    "cough"
}

# Rules: IF conditions THEN conclusion
rules = [
    ({"fever", "cough"}, "flu"),
    ({"flu"}, "take_rest"),
    ({"flu"}, "consult_doctor"),
    ({"fever"}, "high_temperature"),
    ({"cough", "high_temperature"}, "possible_infection")
]


# Forward Chaining Function
def forward_chaining(facts, rules):

    new_fact_added = True

    while new_fact_added:

        new_fact_added = False

        for conditions, conclusion in rules:

            if conditions.issubset(facts):

                if conclusion not in facts:

                    facts.add(conclusion)

                    print("New Fact Generated:", conclusion)

                    new_fact_added = True

    return facts


# Main Program
print("Initial Facts:", facts)

result = forward_chaining(facts, rules)

print("\nFinal Facts:")
for fact in sorted(result):
    print(fact)


# Required Query
query = input("\nEnter a fact to check: ").lower()

if query in result:
    print(query, "is TRUE")
else:
    print(query, "is FALSE")
