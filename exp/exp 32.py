
# Linear Regression Algorithm

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Sample dataset
# X = Hours studied
# Y = Marks obtained

X = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
Y = np.array([35, 40, 50, 55, 65, 70, 80, 85])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, Y)

# Predict values
Y_pred = model.predict(X)

# Display coefficients
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# Predict marks for 9 hours of study
hours = np.array([[9]])
prediction = model.predict(hours)

print("Predicted marks for 9 hours:", prediction[0])

# Evaluate model
print("Mean Squared Error:",
      mean_squared_error(Y, Y_pred))

print("R2 Score:", r2_score(Y, Y_pred))

# Plot graph
plt.scatter(X, Y, color='blue', label='Actual Values')
plt.plot(X, Y_pred, color='red', label='Regression Line')

plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Linear Regression")
plt.legend()
plt.show()
