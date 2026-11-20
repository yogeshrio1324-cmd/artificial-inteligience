
# Support Vector Machine (SVM) for Binary Classification

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import StandardScaler

# Load Breast Cancer dataset
data = datasets.load_breast_cancer()

X = data.data
Y = data.target

# Split dataset into training and testing data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Feature scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Create SVM classifier
model = SVC(kernel='linear')

# Train the model
model.fit(X_train, Y_train)

# Predict test data
Y_pred = model.predict(X_test)

# Display predictions
print("Actual Values:", Y_test[:10])
print("Predicted Values:", Y_pred[:10])

# Calculate accuracy
accuracy = accuracy_score(Y_test, Y_pred)

print("\nAccuracy:", accuracy * 100, "%")

# Display confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(Y_test, Y_pred))

# Classification report
print("\nClassification Report:")
print(classification_report(Y_test, Y_pred,
                            target_names=data.target_names))

# Predict a new sample
new_sample = X_test[:1]

prediction = model.predict(new_sample)

print("New Sample Prediction:",
      data.target_names[prediction[0]])
