
# Dimensionality Reduction using PCA

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# Load Iris dataset
iris = load_iris()

X = iris.data
Y = iris.target

# Display original dimensions
print("Original Dataset Shape:", X.shape)

# Standardize the dataset
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply PCA to reduce dimensions to 2
pca = PCA(n_components=2)

X_pca = pca.fit_transform(X_scaled)

# Display reduced dimensions
print("Reduced Dataset Shape:", X_pca.shape)

# Display explained variance
print("\nExplained Variance Ratio:")
print(pca.explained_variance_ratio_)

print("\nTotal Explained Variance:",
      sum(pca.explained_variance_ratio_) * 100, "%")

# Visualize PCA results
plt.figure(figsize=(8, 6))

for i, name in enumerate(iris.target_names):
    plt.scatter(
        X_pca[Y == i, 0],
        X_pca[Y == i, 1],
        label=name
    )

plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA - Dimensionality Reduction")
plt.legend()
plt.grid()
plt.show()
