# Credit Card Customer Segmentation
This project performs credit card customer segmentation with K Means Clustering. The goal is to cluster customers into distinct groups.

The customers were clustered into three separate groups. To see details on the clusters and cluster and data visualizations, go to "customer_segmentation.ipynb." To see the implementation of the K Means Clustering algorithm, go to the folder "K_Means_Clustering."

## K Means Clustering
The K Means Clustering algorithm is implemented in the "K_Means_Clustering" folder and exported to the K_Means_Clustering package. Sci-kit learn has a built in class "KMeans" that implements the algorithm, but I thought it would be fun to do it myself.

The algorithm starts by assigning random cluster centroids. It then iteratively assigns each data point to its closest centroid. After each round, the centroids are computed as the mean location of every data point in the cluster. The process is repeated until convergence.

## Dataset Description
The dataset can be downloaded here: https://www.kaggle.com/datasets/rupindersinghrana/credit-card-customer-segmentation. It describes the behavior of 660 card holders with 5 features. The dataset can also be found in the "data" folder.

## Results
For detailed results, go to "customer_segmentation.ipynb." For a summary, the customers were clustered into 3 clusters:

- Cluster Red: Low credit customers
- Cluster Blue: Typical Customers
- Cluster Red: Well-off Customers 

The company can use the spending habits of these groups to optimize marketing strategies.