
# K-Nearest Neighbors (KNN) Classification

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

X = iris.data
Y = iris.target

# Split dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, Y_train)

# Predict test data
Y_pred = knn.predict(X_test)

# Display results
print("Actual Values:", Y_test)
print("Predicted Values:", Y_pred)

# Calculate accuracy
accuracy = accuracy_score(Y_test, Y_pred)

print("Accuracy:", accuracy * 100, "%")

# Classification report
print("\nClassification Report:")
print(classification_report(Y_test, Y_pred,
                            target_names=iris.target_names))

# Predict a new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]

prediction = knn.predict(new_sample)

print("New Sample Prediction:",
      iris.target_names[prediction[0]])
