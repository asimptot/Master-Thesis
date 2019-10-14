import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.cluster import KMeans

def findClusterNumber(att):
    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Release Approval')

    X = dataset.iloc[:, [att, 11]].values
    wcss = []
    kume_sayisi_listesi = range(1, 11)
    for i in kume_sayisi_listesi:
        kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)

    plt.plot(kume_sayisi_listesi, wcss)
    plt.title('Clustering Elbow Method for Specifying Cluster Number')
    plt.xlabel('Cluster Number')
    plt.ylabel('Within Clusters Sum of Square (WCSS)')
    plt.show()

print("\nClustering Elbow Method for Genre-Score: ")
findClusterNumber(1)

print("\nClustering Elbow Method for Age-Score: ")
findClusterNumber(2)

print("\nClustering Elbow Method for Experience-Score: ")
findClusterNumber(3)

print("\nClustering Elbow Method for Marriage-Score: ")
findClusterNumber(4)

print("\nClustering Elbow Method for Childbearing-Score: ")
findClusterNumber(5)

print("\nClustering Elbow Method for Graduation-Score: ")
findClusterNumber(6)

print("\nClustering Elbow Method for Former Job-Score: ")
findClusterNumber(7)

print("\nClustering Elbow Method for Seniority-Score: ")
findClusterNumber(8)

print("\nClustering Elbow Method for Title of Arrival-Score: ")
findClusterNumber(9)

print("\nClustering Elbow Method for Estimated Time of Arrival-Score: ")
findClusterNumber(10)