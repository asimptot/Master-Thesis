import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def sex_regression():   #cinsiyete göre skor tahmini

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 1:2].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Sex')
    plt.xlabel('Sex(Male=0, Female=1)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Sex')
    plt.xlabel('Sex(Male=0, Female=1)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Sex')
    plt.xlabel('Sex(Male=0, Female=1)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def age_regression():   #yaşa göre skor tahmini

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 2:3].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Age')
    plt.xlabel('Age')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Age')
    plt.xlabel('Age')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Age')
    plt.xlabel('Age')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def experience_regression():   #çalıştığı toplam yıla göre skor tahmini

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 3:4].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Number of Years Worked')
    plt.xlabel('Number of Years Worked')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Years Worked')
    plt.xlabel('Number of Years Worked')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Years Worked')
    plt.xlabel('Number of Years Worked')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def marriage_regression():   #medeni duruma göre skor tahmini

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 4:5].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Number of Marital Status')
    plt.xlabel('Marital Status (Single=0, Married=1, Divorced=2)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Marital Status')
    plt.xlabel('Marital Status (Single=0, Married=1, Divorced=2)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Marital Status')
    plt.xlabel('Marital Status (Single=0, Married=1, Divorced=2)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def childbearing_regression():   #çocuk sayısına göre skor tahmini

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 5:6].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Number of Children')
    plt.xlabel('Number of Children')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Children')
    plt.xlabel('Number of Children')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Children')
    plt.xlabel('Number of Children')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def graduation_regression():   #mezuniyete göre skor tahmini

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 6:7].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Graduation Grade')
    plt.xlabel('Graduation (Primary=0, High School=1, Bachelors=2, Master=3, Postgraduate=4)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Graduation Grade')
    plt.xlabel('Graduation (Primary=0, High School=1, Bachelors=2, Master=3, Postgraduate=4)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Graduation Grade')
    plt.xlabel('Graduation (Primary=0, High School=1, Bachelors=2, Master=3, Postgraduate=4)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def previous_job_regression():   #önceden çalıştığı iş sayısına göre

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 7:8].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Number of Previous Jobs')
    plt.xlabel('Number of Previous Jobs')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Previous Jobs')
    plt.xlabel('Number of Previous Jobs')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Number of Previous Jobs')
    plt.xlabel('Number of Previous Jobs')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def seniority_regression():   #kıdem derecesine göre skor tahmini

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 8:9].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Seniority Ratio')
    plt.xlabel('Seniority Ratio')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Seniority Ratio')
    plt.xlabel('Seniority Ratio')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Seniority Ratio')
    plt.xlabel('Seniority Ratio')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def title_regression():   #ünvana göre

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 9:10].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Title')
    plt.xlabel('(Technician=0, Engineer=1, Specialist=2, Senior Specialist=3, Architect=4, Senior Architect=5)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Title')
    plt.xlabel('(Technician=0, Engineer=1, Specialist=2, Senior Specialist=3, Architect=4, Senior Architect=5)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Title')
    plt.xlabel('(Technician=0, Engineer=1, Specialist=2, Senior Specialist=3, Architect=4, Senior Architect=5)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

def arrival_regression():   #işe varış süresine göre

    os.chdir(r'D:\Projects\Tez')
    dataset= pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    x = dataset.iloc[:, 10:11].values
    y = dataset.iloc[:, -1].values

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 1/3, random_state=0)
    regressor = LinearRegression()
    regressor.fit(x_train, y_train)

    y_pred = regressor.predict(x_test)
    plt.scatter(x_train, y_train, color='red')
    plt.title('Score Prediction Regression Model According to Arrival Time')
    plt.xlabel('Arrival Time (min)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.scatter(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Arrival Time')
    plt.xlabel('Arrival Time (min)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

    plt.scatter(x_train, y_train, color='red')
    modelin_tahmin_ettigi_y= regressor.predict(x_train)
    plt.plot(x_train, modelin_tahmin_ettigi_y, color='blue')
    plt.title('Score Prediction Regression Model According to Arrival Time')
    plt.xlabel('Arrival Time (min)')
    plt.ylabel('Success Point (1-100)')
    plt.show()

sex_regression()
age_regression()
experience_regression()
marriage_regression()
childbearing_regression()
graduation_regression()
previous_job_regression()
seniority_regression()
title_regression()
arrival_regression()
