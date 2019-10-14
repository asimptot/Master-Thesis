import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder


def dt_recommend():

    dataset = pd.read_excel('Accept.xlsx', sheet_name='Logging')
    dataset.head()

    number = LabelEncoder()
    dataset['Sex'] = number.fit_transform(dataset['Sex'])
    dataset['Marriage'] = number.fit_transform(dataset['Marriage'])
    dataset['Graduation'] = number.fit_transform(dataset['Graduation'])
    dataset['Title'] = number.fit_transform(dataset['Title'])
    dataset['Accept'] = number.fit_transform(dataset['Accept'])

    dataset['Sex'] = dataset['Sex'].astype(float)
    dataset['Marriage'] = dataset['Marriage'].astype(float)
    dataset['Childbearing'] = dataset['Childbearing'].astype(float)
    dataset['Graduation'] = dataset['Graduation'].astype(float)
    dataset['Seniority'] = dataset['Seniority'].astype(float)
    dataset['Title'] = dataset['Title'].astype(float)
    dataset['Age'] = dataset['Age'].astype(float)
    dataset['Experience'] = dataset['Experience'].astype(float)
    dataset['Former Job Quantity'] = dataset['Former Job Quantity'].astype(float)
    dataset['Estimated Time of Arrival'] = dataset['Estimated Time of Arrival'].astype(float)


    x = dataset.iloc[:, 0:1].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)

    sex = input("\nFor Female: 0, For Male: 1\nEnter Gender of Worker: ")

    y_pred1 = regressor.predict(np.array([sex]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", sex, "is= ", y_pred1)


    x = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)

    age = input("\nEnter Age of Worker: ")

    y_pred2 = regressor.predict(np.array([age]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", age, "is= ", y_pred2)


    x = dataset.iloc[:, 2:3].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)

    exp = input("\nEnter Numbers of Years Worked: ")

    y_pred3 = regressor.predict(np.array([exp]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", exp, "is= ", y_pred3)


    x = dataset.iloc[:, 3:4].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)


    mar = input("\nFor Divorced: 0, For Married: 1, For Single: 2\nEnter Marrige Status: ")

    y_pred4 = regressor.predict(np.array([mar]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", mar, "is= ", y_pred4)


    x = dataset.iloc[:, 4:5].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)


    chi = input("\nEnter Numbers of Children: ")

    y_pred5 = regressor.predict(np.array([chi]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", chi, "is= ", y_pred5)

    x = dataset.iloc[:, 5:6].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)


    grad = input("\nFor Bacheloors: 0, For High School: 1, For Master: 2, For PostGraduate: 3, For Primary: 4\nEnter Graduate Status: ")

    y_pred6 = regressor.predict(np.array([grad]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", grad, "is= ", y_pred6)


    x = dataset.iloc[:, 6:7].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)


    job = input("\nEnter Numbers of Previous Jobs: ")

    y_pred7 = regressor.predict(np.array([job]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", job, "is= ", y_pred7)

    x = dataset.iloc[:, 7:8].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)


    sen = input("\nEnter Seniority Level: \n")

    y_pred8 = regressor.predict(np.array([sen]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", sen, "is= ", y_pred8)


    x = dataset.iloc[:, 8:9].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)


    tit = input("\nFor Architect: 0, For Junior: 1, For Senior Architect: 2, For Senior Specialist: 3, For Specialist: 4, For Technician: 5 \nEnter Title of Worker: ")

    y_pred9 = regressor.predict(np.array([tit]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", tit, "is= ", y_pred9)


    x = dataset.iloc[:, 9:10].values
    y = dataset.iloc[:, -1].values

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(x, y)


    est = input("\nEnter Estimated Time of Arrival (min): ")

    y_pred10 = regressor.predict(np.array([est]).reshape(-1, 1))  # 20 yıllık tecrübeli adam
    print("Average score for ", est, "is= ", y_pred10)


    #dizi = [y_pred1, y_pred2, y_pred3, y_pred4, y_pred5, y_pred6, y_pred7, y_pred8, y_pred9, y_pred10]
    #print(dizi)

    toplam= y_pred1+y_pred2+y_pred3+y_pred4+y_pred5+y_pred6+y_pred7+y_pred8+y_pred9+y_pred10
    ort = toplam/10

    print(ort)

    if ort > 0.5:
        print("New Employee can do this task!")

    else:
        print("New Employee cannot do this task!")

dt_recommend()

