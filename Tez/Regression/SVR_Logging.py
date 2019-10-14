import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler


def experience_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 3:4].values
    y = dataset.iloc[:, -1].values

    regressor1 = SVR(kernel='rbf', gamma='auto')
    regressor1.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor1.predict(x), color='blue')
    plt.title('Before Scaling SVR Model')
    plt.xlabel('Numbers of Years Worked')
    plt.ylabel('Score')
    plt.show()

    #After Scaling Process

    sc_X = StandardScaler()
    sc_y = StandardScaler()

    x = sc_X.fit_transform(x)
    y = sc_y.fit_transform(y.reshape(-1, 1))

    regressor2 = SVR(kernel='rbf', gamma='auto')
    regressor2.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor2.predict(x), color='blue')
    plt.title('After Scaling SVR Model')
    plt.xlabel('Numbers of Years Worked')
    plt.ylabel('Score')
    plt.show()

def age_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 2:3].values
    y = dataset.iloc[:, -1].values

    regressor1 = SVR(kernel='rbf', gamma='auto')
    regressor1.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor1.predict(x), color='blue')
    plt.title('Before Scaling SVR Model')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.show()

    #After Scaling Process

    sc_X = StandardScaler()
    sc_y = StandardScaler()

    x = sc_X.fit_transform(x)
    y = sc_y.fit_transform(y.reshape(-1, 1))

    regressor2 = SVR(kernel='rbf', gamma='auto')
    regressor2.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor2.predict(x), color='blue')
    plt.title('After Scaling SVR Model')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.show()

def childbearing_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 5:6].values
    y = dataset.iloc[:, -1].values

    regressor1 = SVR(kernel='rbf', gamma='auto')
    regressor1.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor1.predict(x), color='blue')
    plt.title('Before Scaling SVR Model')
    plt.xlabel('Numbers of Children')
    plt.ylabel('Score')
    plt.show()

    #After Scaling Process

    sc_X = StandardScaler()
    sc_y = StandardScaler()

    x = sc_X.fit_transform(x)
    y = sc_y.fit_transform(y.reshape(-1, 1))

    regressor2 = SVR(kernel='rbf', gamma='auto')
    regressor2.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor2.predict(x), color='blue')
    plt.title('After Scaling SVR Model')
    plt.xlabel('Numbers of Children')
    plt.ylabel('Score')
    plt.show()

def former_job_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 7:8].values
    y = dataset.iloc[:, -1].values

    regressor1 = SVR(kernel='rbf', gamma='auto')
    regressor1.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor1.predict(x), color='blue')
    plt.title('Before Scaling SVR Model')
    plt.xlabel('Numbers of Former Jobs')
    plt.ylabel('Score')
    plt.show()

    #After Scaling Process

    sc_X = StandardScaler()
    sc_y = StandardScaler()

    x = sc_X.fit_transform(x)
    y = sc_y.fit_transform(y.reshape(-1, 1))

    regressor2 = SVR(kernel='rbf', gamma='auto')
    regressor2.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor2.predict(x), color='blue')
    plt.title('After Scaling SVR Model')
    plt.xlabel('Numbers of Former Jobs')
    plt.ylabel('Score')
    plt.show()

def est_arr_time_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 10:11].values
    y = dataset.iloc[:, -1].values

    regressor1 = SVR(kernel='rbf', gamma='auto')
    regressor1.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor1.predict(x), color='blue')
    plt.title('Before Scaling SVR Model')
    plt.xlabel('Estimated Arrival Time')
    plt.ylabel('Score')
    plt.show()

    #After Scaling Process

    sc_X = StandardScaler()
    sc_y = StandardScaler()

    x = sc_X.fit_transform(x)
    y = sc_y.fit_transform(y.reshape(-1, 1))

    regressor2 = SVR(kernel='rbf', gamma='auto')
    regressor2.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor2.predict(x), color='blue')
    plt.title('After Scaling SVR Model')
    plt.xlabel('Estimated Arrival Time')
    plt.ylabel('Score')
    plt.show()

def seniority_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 8:9].values
    y = dataset.iloc[:, -1].values

    regressor1 = SVR(kernel='rbf', gamma='auto')
    regressor1.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor1.predict(x), color='blue')
    plt.title('Before Scaling SVR Model')
    plt.xlabel('Seniority')
    plt.ylabel('Score')
    plt.show()

    #After Scaling Process

    sc_X = StandardScaler()
    sc_y = StandardScaler()

    x = sc_X.fit_transform(x)
    y = sc_y.fit_transform(y.reshape(-1, 1))

    regressor2 = SVR(kernel='rbf', gamma='auto')
    regressor2.fit(x, y)

    plt.scatter(x, y, color='red')
    plt.plot(x, regressor2.predict(x), color='blue')
    plt.title('After Scaling SVR Model')
    plt.xlabel('Seniority')
    plt.ylabel('Score')
    plt.show()


experience_decision()
age_decision()
childbearing_decision()
former_job_decision()
est_arr_time_decision()
seniority_decision()