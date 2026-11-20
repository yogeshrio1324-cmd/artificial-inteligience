
# Image Classification using Neural Network
# TensorFlow and Keras

import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# Normalize image data
x_train = x_train / 255.0
x_test = x_test / 255.0

# Create Neural Network model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),

    keras.layers.Dense(128, activation='relu'),

    keras.layers.Dense(64, activation='relu'),

    keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=32
)

# Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)

print("Test Accuracy:", test_accuracy * 100, "%")

# Predict an image
prediction = model.predict(x_test[:1])

predicted_class = prediction.argmax()

print("Predicted Digit:", predicted_class)
print("Actual Digit:", y_test[0])

# Display the image
plt.imshow(x_test[0], cmap='gray')
plt.title("Predicted Digit: " + str(predicted_class))
plt.axis('off')
plt.show()
