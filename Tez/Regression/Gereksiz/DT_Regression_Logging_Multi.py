import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

#DT'de veriler grafik uzerinde ciktiginda1n scaler'a ihtiyac yoktur

def decision_tree_suggest(): #male-25-15-Divorced-1-Master-5-2-Junior-20 => Scaler örnek

    dataset = pd.read_excel('Accept.xlsx', sheet_name='Logging')
    dataset.head()

    number = LabelEncoder()
    dataset['Sex'] = number.fit_transform(dataset['Sex'])
    dataset['Marriage'] = number.fit_transform(dataset['Marriage'])
    dataset['Childbearing'] = number.fit_transform(dataset['Childbearing'])
    dataset['Graduation'] = number.fit_transform(dataset['Graduation'])
    dataset['Seniority'] = number.fit_transform(dataset['Seniority'])
    dataset['Title'] = number.fit_transform(dataset['Title'])
    dataset['Age'] = number.fit_transform(dataset['Age'])
    dataset['Experience'] = number.fit_transform(dataset['Experience'])
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


    features = ["Sex", "Age", "Experience", "Marriage", "Childbearing", "Graduation", "Former Job Quantity",
                "Seniority", "Title", "Estimated Time of Arrival"]
    target = "Accept"


    scaled_features = dataset.copy()
    col_names = ['Age', 'Experience', 'Childbearing', 'Former Job Quantity', 'Seniority', 'Estimated Time of Arrival', 'Sex',
                 'Marriage', 'Childbearing', 'Graduation', 'Title']
    normalize = scaled_features[col_names]
    scaler = StandardScaler().fit(normalize.values)
    normalize = scaler.transform(normalize.values)

    #for i in range(len(dataset)):
    #    dataset['Age'].values[i] = normalize[i][0]
    #    dataset['Experience'].values[i] = normalize[i][1]
    #    dataset['Childbearing'].values[i] = normalize[i][2]
    #    dataset['Former Job Quantity'].values[i] = normalize[i][3]
    #    dataset['Seniority'].values[i] = normalize[i][4]
    #    dataset['Estimated Time of Arrival'].values[i] = normalize[i][5]
    #    dataset['Title'].values[i] = normalize[i][10]
    #    dataset['Sex'].values[i] = normalize[i][6]
    #    dataset['Marriage'].values[i] = normalize[i][7]
    #    dataset['Childbearing'].values[i] = normalize[i][8]
    #    dataset['Graduation'].values[i] = normalize[i][9]


    features_train, features_test, target_train, target_test = train_test_split(dataset[features], dataset[target],
                                                                                test_size=0.33, random_state=0)

    regressor = DecisionTreeRegressor(random_state=0)
    regressor.fit(features_train, target_train)

    sex = input("Enter Gender of Worker: \nFor Female: 0, For Male: 1\n")
    age = input("Enter Age of Worker: \n")
    exp = input("Enter Numbers of Years Worked: \n")
    mar = input("Enter Marrige Status: \n For Divorced: 0, For Married: 1, For Single: 2\n")
    chi = input("Enter Numbers of Children: \n")
    gra = input(
        "Enter Graduate Status: \n For Bacheloors: 0, For High School: 1, For Master: 2, For PostGraduate: 3, For Primary: 4\n")
    pre = input("Enter Numbers of Previous Jobs: \n")
    sen = input("Enter Seniority Level: \n")
    tit = input(
        "Enter Title of Worker: \n For Architect: 0, For Junior: 1, For Senior Architect: 2, For Senior Specialist: 3, For Specialist: 4, For Technician: 5 \n")
    arr = input("Enter Estimated Time of Arrival (min): \n")


    result = (regressor.predict(
        [[float(sex), float(age), float(exp), float(mar), float(chi), float(gra), float(pre), float(sen), float(tit), float(arr)]]))

    pred = regressor.predict(features_test)
    accuracy = accuracy_score(target_test, pred)

    print("Accuracy: ", accuracy)
    print("Pred: ", pred)

    sum = 0
    for i in range(len(pred)):
        sum = int(sum) + int(pred[i])
    test_size = 0.33
    compare = len(features_test) / test_size
    if float(sum / compare) > 0.5:
        print("TUTKU\nYes!")
    else:
        print("TUTKU\nNo!")

    print(result)

    if result == 1:
        print("New Employee can do this task!")

    else:
        print("New Employee cannot do this task!")



decision_tree_suggest()