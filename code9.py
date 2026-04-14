from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Features only
X = df[['Feature1','Feature2','Feature3','Feature4']]

# Standardize
X_scaled = StandardScaler().fit_transform(X)

# Apply PCA
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

print("Explained Variance Ratio:", pca.explained_variance_ratio_)
print("Transformed Data:\n", components)
