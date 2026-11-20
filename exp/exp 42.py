
# K-Means Clustering Algorithm

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate sample dataset
X, Y = make_blobs(
    n_samples=100,
    centers=3,
    n_features=2,
    random_state=42
)

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train the model
kmeans.fit(X)

# Predict cluster labels
labels = kmeans.predict(X)

# Display cluster centers
print("Cluster Centers:")
print(kmeans.cluster_centers_)

# Display cluster labels
print("\nCluster Labels:")
print(labels)

# Display number of clusters
print("\nNumber of Clusters:", kmeans.n_clusters)

# Visualize the clusters
plt.figure(figsize=(8, 6))

plt.scatter(
    X[:, 0],
    X[:, 1],
    c=labels,
    cmap='viridis',
    s=50
)

# Plot cluster centers
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    color='red',
    marker='X',
    s=200,
    label='Centroids'
)

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
