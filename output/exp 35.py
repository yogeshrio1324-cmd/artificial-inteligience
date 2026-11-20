
# Decision Tree Classification Algorithm

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt

# Load Iris dataset
iris = load_iris()

X = iris.data
Y = iris.target

# Split dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create Decision Tree classifier
model = DecisionTreeClassifier(
    criterion='entropy',
    random_state=42
)

# Train the model
model.fit(X_train, Y_train)

# Predict test data
Y_pred = model.predict(X_test)

# Display predictions
print("Actual Values:", Y_test)
print("Predicted Values:", Y_pred)

# Calculate accuracy
accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy:", accuracy * 100, "%")

# Predict a new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(new_sample)

print("Predicted Flower:",
      iris.target_names[prediction[0]])

# Visualize Decision Tree
plt.figure(figsize=(15, 8))

tree.plot_tree(
    model,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)

plt.title("Decision Tree Classification")
plt.show()
