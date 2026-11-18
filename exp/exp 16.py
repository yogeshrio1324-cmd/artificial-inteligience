# Feed Forward Neural Network

from sklearn.neural_network import MLPClassifier

# Training data
X = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]

# Output data (XOR operation)
y = [0, 1, 1, 0]

# Create Feed Forward Neural Network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation='relu',
    solver='lbfgs',
    max_iter=5000,
    random_state=1
)

# Train the model
model.fit(X, y)

# Test the model
print("Feed Forward Neural Network Output:")

for data in X:
    prediction = model.predict([data])
    print(data, "=", prediction[0])
