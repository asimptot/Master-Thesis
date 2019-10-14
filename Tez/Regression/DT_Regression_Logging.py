import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor

def experience_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 3:4].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)

    x_grid = np.arange(min(x), max(x), 0.01)
    x_grid = x_grid.reshape((len(x_grid), 1))
    plt.scatter(x, y, color='red')
    plt.plot(x_grid, regressor.predict(x_grid), color='blue')
    plt.title('Decision Tree Regression')
    plt.xlabel('Numbers of Years Worked')
    plt.ylabel('Score')
    plt.show()

    exp = input("Enter Numbers of Years Worked: ")

    y_pred = regressor.predict(np.array([exp]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", exp, "is= ", y_pred)

def sex_decision():
    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)

    x_grid = np.arange(min(x), max(x), 0.01)
    x_grid = x_grid.reshape((len(x_grid), 1))
    plt.scatter(x, y, color='red')
    plt.plot(x_grid, regressor.predict(x_grid), color='blue')
    plt.title('Decision Tree Regression')
    plt.xlabel('Sex')
    plt.ylabel('Score')
    plt.show()

    sex = input("Select sex type (Male=0, Female=1) ")

    y_pred = regressor.predict(np.array([sex]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", sex, "is= ", y_pred)

def age_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 2:3].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)

    x_grid = np.arange(min(x), max(x), 0.01)
    x_grid = x_grid.reshape((len(x_grid), 1))
    plt.scatter(x, y, color='red')
    plt.plot(x_grid, regressor.predict(x_grid), color='blue')
    plt.title('Decision Tree Regression')
    plt.xlabel('Age')
    plt.ylabel('Score')
    plt.show()

    age = input("Enter Age: ")

    y_pred = regressor.predict(np.array([age]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", age, "is= ", y_pred)

def marriage_decision():

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 4:5].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)

    x_grid = np.arange(min(x), max(x), 0.01)
    x_grid = x_grid.reshape((len(x_grid), 1))
    plt.scatter(x, y, color='red')
    plt.plot(x_grid, regressor.predict(x_grid), color='blue')
    plt.title('Decision Tree Regression')
    plt.xlabel('Marriage')
    plt.ylabel('Score')
    plt.show()

    mar = input("Enter Maritial Status: ")

    y_pred = regressor.predict(np.array([mar]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", mar, "is= ", y_pred)

#sex_decision()
#age_decision()
experience_decision()
#marriage_decision()
