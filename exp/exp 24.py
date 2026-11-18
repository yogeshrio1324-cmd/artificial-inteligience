# Diet Suggestion System Based on Disease

# Diet database
diet = {
    "diabetes": [
        "Whole grains",
        "Green vegetables",
        "Beans",
        "Nuts",
        "Low-sugar fruits"
    ],

    "hypertension": [
        "Fresh fruits",
        "Green vegetables",
        "Low-salt foods",
        "Whole grains",
        "Low-fat dairy"
    ],

    "obesity": [
        "Vegetable salad",
        "Fruits",
        "Whole grains",
        "Boiled vegetables",
        "Protein-rich foods"
    ],

    "anemia": [
        "Spinach",
        "Beans",
        "Iron-fortified foods",
        "Lentils",
        "Vitamin C-rich fruits"
    ],

    "heart disease": [
        "Fresh fruits",
        "Vegetables",
        "Whole grains",
        "Nuts",
        "Low-saturated-fat foods"
    ]
}


# Function to suggest diet
def suggest_diet(disease):

    disease = disease.lower()

    if disease in diet:
        print("\nDiet Suggestions for", disease.capitalize())

        for food in diet[disease]:
            print("-", food)

    else:
        print("Disease not found in database.")


# Main Program
print("DIET SUGGESTION SYSTEM")
print("----------------------")

print("Available Diseases:")
for disease in diet:
    print("-", disease.capitalize())

disease = input("\nEnter the disease: ")

suggest_diet(disease)
