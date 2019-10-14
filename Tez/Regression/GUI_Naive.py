import numpy as np
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tkinter import *

def butonKomutlari():
    sex = giris1.get()
    age = giris2.get()
    exp = giris3.get()
    mar = giris4.get()
    chi = giris5.get()
    gra = giris6.get()
    pre = giris7.get()
    sen = giris8.get()
    tit = giris9.get()
    arr = giris10.get()

    sayi1 = 0
    sayi2 = 0
    sayi3 = 0
    sayi4 = 0
    sayi5 = 0
    sayi6 = 0
    sayi7 = 0
    sayi8 = 0
    sayi9 = 0
    sayi10 = 0

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
    features = ["Sex", "Age", "Experience", "Marriage", "Childbearing", "Graduation", "Former Job Quantity",
                "Seniority", "Title", "Estimated Time of Arrival"]
    target = "Accept"

    features_train, features_test, target_train, target_test = train_test_split(dataset[features], dataset[target],
                                                                                test_size=0.33, random_state=54)

    model = GaussianNB()
    model.fit(features_train, target_train)

    pred = model.predict(features_test)
    accuracy = accuracy_score(target_test, pred)

    try:
        sayi1 = int(sex)
    except:
        print("Fill in the blank!")
    try:
        sayi2 = int(age)
    except:
        print("Fill in the blank!")

    try:
        sayi3 = int(exp)
    except:
        print("Fill in the blank!")

    try:
        sayi4 = int(mar)
    except:
        print("Fill in the blank!")

    try:
        sayi5 = int(chi)
    except:
        print("Fill in the blank!")

    try:
        sayi6 = int(gra)
    except:
        print("Fill in the blank!")

    try:
        sayi7 = int(pre)
    except:
        print("Fill in the blank!")

    try:
        sayi8 = int(sen)
    except:
        print("birincide sayı girilmemiş")

    try:
        sayi9 = int(tit)
    except:
        print("birincide sayı girilmemiş")

    try:
        sayi10 = int(arr)
    except:
        print("birincide sayı girilmemiş")

    sonuc = (model.predict([[sayi1, sayi2, sayi3, sayi4, sayi5, sayi6, sayi7, sayi8, sayi9, sayi10]]))
    cevap.set(sonuc)

    if sonuc == 1:
        cevap.set("New Employee can do this task!")

    else:
        cevap.set("New Employee cannot do this task!")

p = Tk()
p.title("Classification User Interface")
p.geometry("750x500+500+200")

bilgilendirme = Label(p, text="Worker Prediction System")
bilgilendirme.grid(row=0, column=0, columnspan=2)

bilgilendirme1 = Label(p, text="Female: 0, Male: 1")
bilgilendirme1.grid(row=1, column=2, columnspan=1)
s1Lbl = Label(p, text="Gender: ")
s1Lbl.grid(row=1, column=0)


s2Lbl = Label(p, text="Age: ")
s2Lbl.grid(row=2, column=0)

s3Lbl = Label(p, text="Experience: ")
s3Lbl.grid(row=3, column=0)

bilgilendirme2 = Label(p, text="Divorced: 0, Married: 1, Single: 2")
bilgilendirme2.grid(row=4, column=2, columnspan=1)
s4Lbl = Label(p, text="Maritial Status: ")
s4Lbl.grid(row=4, column=0)

s5Lbl = Label(p, text="Numbers of Children: ")
s5Lbl.grid(row=5, column=0)

bilgilendirme3 = Label(p, text="Bacheloors: 0, High School: 1, Master: 2, Primary: 3")
bilgilendirme3.grid(row=6, column=2, columnspan=1)
s6Lbl = Label(p, text="Graduate Status: ")
s6Lbl.grid(row=6, column=0)

s7Lbl = Label(p, text="Numbers of Previous Jobs: ")
s7Lbl.grid(row=7, column=0)

s8Lbl = Label(p, text="Seniority Level: ")
s8Lbl.grid(row=8, column=0)

bilgilendirme4 = Label(p, text="Architect: 0, Junior: 1, Senior Architect: 2, Senior Specialist: 3, Specialist: 4, Technician: 5")
bilgilendirme4.grid(row=9, column=2, columnspan=1)
s9Lbl = Label(p, text="Title: ")
s9Lbl.grid(row=9, column=0)

s10Lbl = Label(p, text="Arrival Time: ")
s10Lbl.grid(row=10, column=0)

giris1 = Entry(p)
giris1.grid(row=1, column=1)

giris2 = Entry(p)
giris2.grid(row=2, column=1)

giris3 = Entry(p)
giris3.grid(row=3, column=1)

giris4 = Entry(p)
giris4.grid(row=4, column=1)

giris5 = Entry(p)
giris5.grid(row=5, column=1)

giris6 = Entry(p)
giris6.grid(row=6, column=1)

giris7 = Entry(p)
giris7.grid(row=7, column=1)

giris8 = Entry(p)
giris8.grid(row=8, column=1)

giris9 = Entry(p)
giris9.grid(row=9, column=1)

giris10 = Entry(p)
giris10.grid(row=10, column=1)

cevap = StringVar()
cevap.set("Not Calculated Yet")

sonucLbl = Label(p, text="Result: ")
sonucLbl.grid(row=11, column=0)

cevapLbl = Label(p, textvariable=cevap)
cevapLbl.grid(row=11, column=1, sticky=W)

dugme = Button(p, text="Calculate", command=butonKomutlari)
dugme.grid(row=12, column=1, sticky=E)


p.mainloop()
