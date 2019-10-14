import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

dataset = pd.read_excel('Accept.xlsx', sheet_name='Logging')
dataset.head()

number = LabelEncoder()
dataset['Sex'] = number.fit_transform(dataset['Sex'])
dataset['Age'] = number.fit_transform(dataset['Age'])
dataset['Experience'] = number.fit_transform(dataset['Experience'])
dataset['Marriage'] = number.fit_transform(dataset['Marriage'])
dataset['Childbearing'] = number.fit_transform(dataset['Childbearing'])
dataset['Graduation'] = number.fit_transform(dataset['Graduation'])
dataset['Former Job Quantity'] = number.fit_transform(dataset['Former Job Quantity'])
dataset['Seniority'] = number.fit_transform(dataset['Seniority'])
dataset['Title'] = number.fit_transform(dataset['Title'])
dataset['Estimated Time of Arrival'] = number.fit_transform(dataset['Estimated Time of Arrival'])

dataset['Accept'] = number.fit_transform(dataset['Accept'])
features = ["Sex", "Age", "Experience", "Marriage", "Childbearing", "Graduation", "Former Job Quantity", "Seniority", "Title", "Estimated Time of Arrival"]
target = "Accept"

features_train, features_test, target_train, target_test = train_test_split(dataset[features], dataset[target],
                                                                            test_size = 0.33, random_state = 0)

model = GaussianNB()
model.fit(features_train, target_train)

pred = model.predict(features_test)
accuracy = accuracy_score(target_test, pred)

sex = input("Enter Gender of Worker: \nFor Female: 0, For Male: 1\n")
age = input("Enter Age of Worker: \n")
exp = input("Enter Numbers of Years Worked: \n")
mar = input("Enter Marrige Status: \n For Divorced: 0, For Married: 1, For Single: 2\n")
chi = input("Enter Numbers of Children: \n")
gra = input("Enter Graduate Status: \n For Bacheloors: 0, For High School: 1, For Master: 2, For PostGraduate: 3, For Primary: 4\n")
pre = input("Enter Numbers of Previous Jobs: \n")
sen = input("Enter Seniority Level: \n")
tit = input("Enter Title of Worker: \n For Architect: 0, For Junior: 1, For Senior Architect: 2, For Senior Specialist: 3, For Specialist: 4, For Technician: 5 \n")
arr = input("Enter Estimated Time of Arrival (min): \n")

result = (model.predict([[int(sex), int(age), int(exp), int(mar), int(chi), int(gra), int(pre), int(sen), int(tit), int(arr)]]))

print(result)

if result == 1:
    print("New Employee can do this task!")

else:
    print("New Employee cannot do this task!")
