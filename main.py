1-topshiriq: Guruh ro‘yxati ma’lumotlarini tayyorlash va tahrirlash
 pandas as pd
import numpy as np

# Guruh ro‘yxati
data = {
    "Ism": ["Ali", "Vali", "Hasan", "Husan"],
    "Familiya": ["Aliyev", "Valiyev", "Hasanov", "Husanov"],
    "Yosh": [20, 21, 19, 22],
    "Baho": [85, 90, 78, 88]
}

df = pd.DataFrame(data)
print(df)
# O‘rtacha bahoni hisoblash
ortalacha_baho = np.mean(df["Baho"])
print("O‘rtacha baho:", ortalacha_baho)

# 80 dan yuqori baho olganlarni ajratish
yaxshi_talabalar = df[df["Baho"] > 80]
print(yaxshi_talabalar)

# Yoshga 1 yil qo‘shish
df["Yosh"] = df["Yosh"] + 1
print(df)

2-topshiriq:Mashina markalari ma’lumotlarini tayyorlash va tahrirlash
import pandas as pd
import numpy as np

cars = {
    "Marka": ["Toyota", "BMW", "Chevrolet", "Mercedes"],
    "Model": ["Camry", "X5", "Malibu", "E-Class"],
    "Yil": [2020, 2019, 2021, 2018],
    "Narx": [30000, 55000, 28000, 60000]
}

df_cars = pd.DataFrame(cars)
print(df_cars)
import pandas as pd
import numpy as np

cars = {
    "Marka": ["Toyota", "BMW", "Chevrolet", "Mercedes"],
    "Model": ["Camry", "X5", "Malibu", "E-Class"],
    "Yil": [2020, 2019, 2021, 2018],
    "Narx": [30000, 55000, 28000, 60000]
}

df_cars = pd.DataFrame(cars)
print(df_cars)


