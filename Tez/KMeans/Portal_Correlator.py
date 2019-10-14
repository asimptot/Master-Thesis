import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.cluster import KMeans
import seaborn as sns

def sex():

    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')

    X = dataset.iloc[:, [1, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Normal')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Unsuccessful')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Successful')
    # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Küme 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Küme 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
                label='Centroids')
    plt.title('Tester Sex-Score Segmentation for Logging Test')
    plt.xlabel('Sex(Male=0, Female=1)')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def age():

    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')
    X = dataset.iloc[:, [2, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=4, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=100, c='cyan', label='Cluster 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Küme 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
                label='Centroids')
    plt.title('Tester Age-Score Segmentation for Logging Test')
    plt.xlabel('Age')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def experience():

    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')

    X = dataset.iloc[:, [3, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    #plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    #plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
               label='Centroids')
    plt.title('Tester Experience-Score Segmentation for Logging Test')
    plt.xlabel('Numbers of Years Worked')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def marriage():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')

    X = dataset.iloc[:, [4, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
               label='Centroids')
    plt.title('Tester Marital Status-Score Segmentation for Logging Test')
    plt.xlabel('Marital Status (Single=0, Married=1, Divorced=2)')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def childbearing():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')

    X = dataset.iloc[:, [5, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
                label='Centroids')
    plt.title('Tester Childbearing-Score Segmentation for Logging Test')
    plt.xlabel('Number of Children')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def graduation():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')
    X = dataset.iloc[:, [6, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
# plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
# plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
            label='Centroids')
    plt.title('Tester Graduation-Score Segmentation for Logging Test')
    plt.xlabel('Graduation (Primary=0, High School=1, Bachelors=2, Master=3, Postgraduate=4)')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def previous_job():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    X = dataset.iloc[:, [7, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
                label='Centroids')
    plt.title('Tester Previous Job-Score Segmentation for Logging Test')
    plt.xlabel('Number of Previous Jobs')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def seniority():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    X = dataset.iloc[:, [8, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
                label='Centroids')
    plt.title('Tester Seniority-Score Segmentation for Logging Test')
    plt.xlabel('Seniority Ratio')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def title():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    X = dataset.iloc[:, [9, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
                label='Centroids')
    plt.title('Tester Title-Score Segmentation for Logging Test')
    plt.xlabel('(Technician=0, Engineer=1, Specialist=2, Senior Specialist=3, Architect=4, Senior Architect=5)')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def arrival_time():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')

    X = dataset.iloc[:, [10, 11]].values
    wcss = []
    list_of_cluster_number = range(1, 11)

    kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300, n_init=10, random_state=0)
    y_kmeans = kmeans.fit_predict(X)

    plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
    plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
    plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')
    # plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
    # plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow',
               label='Centroids')
    plt.title('Tester Time of Arrival-Score Segmentation for Logging Test')
    plt.xlabel('Arrival Time (min)')
    plt.ylabel('Success Point (1-100)')
    plt.legend()
    plt.show()

def age_sex():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Portal')

    plt.figure(figsize=(8, 4))
    sns.scatterplot(x="Age", y="Score", hue="Sex", data=dataset)
    plt.show()

def exp_mar():
    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    plt.figure(figsize=(8, 4))
    sns.scatterplot(x="Experience", y="Score", hue="Marriage", data=dataset)
    plt.show()

sex()
age()
experience()
marriage()
childbearing()
graduation()
previous_job()
seniority()
title()
arrival_time()
age_sex()
exp_mar()
