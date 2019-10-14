import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from sklearn.tree import DecisionTreeRegressor
from tkinter import *


def butonKomutlari():
    sex = giris1.get()
    age = giris2.get()

    sayi1 = 0
    sayi2 = 0

    os.chdir(r'D:\Projects\Tez')
    dataset = pd.read_excel('Attributes.xlsx', sheet_name='Logging')

    try:
        sayi1 = int(sex)
        x = dataset.iloc[:, 1:2].values
        y = dataset.iloc[:, -1].values
        regressor = DecisionTreeRegressor(random_state=0)
        regressor.fit(x, y)

        x_grid = np.arange(min(x), max(x), 0.01)
        x_grid = x_grid.reshape((len(x_grid), 1))
    except:
        print("Fill in the blank!")
    try:
        sayi2 = int(age)
        x = dataset.iloc[:, 2:3].values
        y = dataset.iloc[:, -1].values
        regressor = DecisionTreeRegressor(random_state=0)
        regressor.fit(x, y)

        x_grid = np.arange(min(x), max(x), 0.01)
        x_grid = x_grid.reshape((len(x_grid), 1))
    except:
        print("Fill in the blank!")

    sonuc = regressor.predict(np.array([sayi1]).reshape(-1, 1))
    cevap.set(sonuc)

    sonuc = regressor.predict(np.array([sayi2]).reshape(-1, 1))
    cevap.set(sonuc)

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

giris1 = Entry(p)
giris1.grid(row=1, column=1)

giris2 = Entry(p)
giris2.grid(row=2, column=1)

cevap = StringVar()
cevap.set("Not Calculated Yet")

sonucLbl = Label(p, text="Result: ")
sonucLbl.grid(row=11, column=0)

cevapLbl = Label(p, textvariable=cevap)
cevapLbl.grid(row=11, column=1, sticky=W)

dugme = Button(p, text="Calculate", command=butonKomutlari)
dugme.grid(row=12, column=1, sticky=E)

p.mainloop()
