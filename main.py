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
import zipfile
import os


4-amaliy mashg'ulot
# 1-TOPSHIRIQ: Ma'lumotlarni siqish (Ziplash)
filename = "malumot.txt"
with open(filename, "w") as f:
    f.write("Bu amaliy ish uchun yaratilgan test ma'lumoti. " * 100)

zip_name = "arxiv.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    zipf.write(filename, compress_type=zipfile.ZIP_DEFLATED)

print(f"1. {filename} fayli {zip_name} ichiga siqildi.")

# 2-TOPSHIRIQ: Siqilgan faylni ochish va tekshirish
with zipfile.ZipFile(zip_name, 'r') as zipf:
    zipf.extractall("ochilgan_fayllar")
    content = zipf.namelist()

# Xulosa
original_size = os.path.getsize(filename)
zip_size = os.path.getsize(zip_name)

print("\n--- XULOSA ---")
print(f"Asl fayl hajmi: {original_size} bayt")
print(f"Siqilgan fayl hajmi: {zip_size} bayt")
print(f"Natija: Fayl hajmi {((original_size - zip_size) / original_size) * 100:.2f}% ga kamaydi.")


