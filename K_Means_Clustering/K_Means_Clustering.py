import numpy as np

class K_Means_Clustering():
    def __init__(self, n_clusters, max_iter=300, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
    
    def fit(self, X):
        # initialize random points as first centroids
        self.centroids = X[np.random.choice(len(X), self.n_clusters, replace=False)]

        # iterate and run through clustering
        for i in range(self.max_iter):
            # assign points to nearest clusters
            clusters = self.assign_clusters(X)

            # update centroids
            new_centroids = self.update_centroids(X, clusters)

            # Check for convergence
            if np.linalg.norm(new_centroids - self.centroids) < self.tol:
                break
            
            self.centroids = new_centroids
    
    def assign_clusters(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        return np.argmin(distances, axis=0)
    
    def update_centroids(self, X, clusters):
        new_centroids = np.zeros_like(self.centroids)

        for i in range(self.n_clusters):
            new_centroids[i] = np.mean(X[clusters == i], axis=0)

        return new_centroids
    
    def compute_inertia(self, X):
        distances = np.sqrt(((X - self.centroids[:, np.newaxis])**2).sum(axis=2))
        min_distances = np.min(distances, axis=0)
        inertia = np.sum(min_distances ** 2)
        
        return inertia