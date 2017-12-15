import numpy as np

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

np.random.seed(111)

# Create dummy data set
X, y = make_blobs(n_samples=100, n_features=2, centers=2, cluster_std=5.0, random_state=111)

# Visualize sample data set
plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, edgecolor='k')
plt.show()

# Standardize data set
scaler = StandardScaler(with_std=False)
X_Standardized = scaler.fit_transform(X)

# Compute eigen values and eigen vectors
covariance_matrix = np.cov(X_Standardized.T)
eigen_values, eigen_vectors = np.linalg.eig(covariance_matrix)

print('Eigen Values  : ' + str(eigen_values))
print('Eigen Vectors : \n' + str(eigen_vectors))
