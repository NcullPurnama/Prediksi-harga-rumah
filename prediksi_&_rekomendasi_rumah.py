# -*- coding: utf-8 -*-
"""Prediksi & Rekomendasi Rumah.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_uU2wzA0mAyqa57OWL-7fBHbcbsdIizr

# Library

Pertama kita import library yang dibutuhkan untuk membuat model prediksi harga rumah
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import files
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

"""# Dataset"""

files.upload()

!mkdir -p ~/.kaggle
!cp kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d nafisbarizki/daftar-harga-rumah-jabodetabek

"""Import dataset yang di download dari Kaggle"""

!unzip daftar-harga-rumah-jabodetabek.zip

"""Hasil dari download tadi berupa ZIP makadari itu kita perlu melakukan unzip supaya dataset dapat digunakan"""

df = pd.read_csv('jabodetabek_house_price.csv')

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])

"""Insight

---
Dari code diatas dapat kita ketahui kalau dataset yang digunakan terdiri dari 3553 data dan 27 kolom

# Exploratory Data Analysis (EDA)

Exploratory data analysis merupakan proses investigasi awal pada data untuk menganalisis karakteristik, menemukan pola, anomali, dan memeriksa asumsi pada data. Teknik ini biasanya menggunakan bantuan statistik dan representasi grafis atau visualisasi.
"""

df.head()

df.info()

df.shape

df.isnull().sum()

df.describe()

df.duplicated().sum()

"""Insight
---

Dari info diatas, tidak terdapat data duplikat pada dataset, namun sepertinya masih ada data yanag kosong

# **Pre cleaning**
"""

df_clean = df.copy()

"""Kolom 'url', 'title', 'address', 'ads_id', 'year_built' tidak relevan untuk membuat model, oleh karena itu kita drop kolomnya"""

# Drop kolom yang tidak relevan untuk prediksi harga
drop_cols = ['url', 'title', 'address', 'ads_id', 'year_built']
df_clean.drop(columns=drop_cols, inplace=True)

"""## Memperbaiki tipe data

Dari info df diatas dapat kita lihat kalau kolom 'bedrooms', 'bathrooms', 'maid_bedrooms', 'maid_bathrooms','floors', 'building_age', 'garages', 'carports' masih berupa float64, untuk pembuatan model kita ganti tipe datanya menjadi Integer
"""

# Kolom numerik yang harusnya integer
int_cols = [
    'bedrooms', 'bathrooms', 'maid_bedrooms', 'maid_bathrooms',
    'floors', 'building_age', 'garages', 'carports'
]
for col in int_cols:
    df_clean[col] = df_clean[col].astype('Int64')

"""Dan untuk kolom 'district', 'city', 'property_type', 'certificate', 'property_condition', 'building_orientation', 'furnishing'kita ubah juga menjadi category"""

# Kolom kategori
cat_cols = [
    'district', 'city', 'property_type', 'certificate',
    'property_condition', 'building_orientation', 'furnishing'
]
for col in cat_cols:
    df_clean[col] = df_clean[col].astype('category')

df_clean['electricity'] = (df_clean['electricity'].astype(str).str.extract(r'(\d+)').astype('Int64'))

df_clean.head()

df_clean.info()

print("Kolom setelah pre-cleaning:")
print(df_clean.columns.tolist())

"""Setelah selesai memperbaiki tipe data, maka kolom 'price_in_rp', 'district', 'city', 'lat', 'long', 'facilities', 'property_type', 'bedrooms', 'bathrooms', 'land_size_m2', 'building_size_m2', 'carports', 'certificate', 'electricity', 'maid_bedrooms', 'maid_bathrooms', 'floors', 'building_age', 'property_condition', 'building_orientation', 'garages', 'furnishing' siap digunakan dalam pembuatan model"""

# Mengambil salah satu kolom secara acak

pd.set_option('display.max_columns', None)
df_clean.iloc[0]

"""# EDA Univariate

## **Distrbusi Harga Rumah**
"""

plt.figure(figsize=(10, 5))
sns.histplot(df_clean['price_in_rp'], bins=50, kde=True)
plt.title('Distribusi Harga Rumah')
plt.xlabel('Harga (Rp)')
plt.ylabel('Jumlah Properti')
plt.show()

"""insight

---
Dari plot diatas dapat kita lihat grafik distribusi harga rumah menunjukkan bahwa mayoritas rumah yang dijual berada pada rentang harga di bawah Rp 10 miliar. Distribusi bersifat miring ke kanan (right-skewed), dengan sedikit rumah yang memiliki harga ekstrem hingga mencapai lebih dari Rp 100 miliar. Hal ini mengindikasikan adanya outlier dalam data, serta pentingnya mempertimbangkan transformasi data seperti logaritma saat membangun model prediksi agar performa model tidak terdistorsi oleh harga ekstrem.

## **Distribusi numerik**
"""

numeric_cols = ['bedrooms', 'bathrooms', 'land_size_m2', 'building_size_m2',
                'carports', 'floors', 'maid_bedrooms', 'maid_bathrooms',
                'garages', 'electricity', 'building_age']

for col in numeric_cols:
    plt.figure(figsize=(6, 4))
    sns.histplot(df_clean[col], bins=30, kde=True)
    plt.title(f'Distribusi {col}')
    plt.xlabel(col)
    plt.ylabel('Jumlah Properti')
    plt.show()

"""Insight

---

- plot kamar tidur
> Mayoritas rumah memiliki 2 hingga 3 kamar tidur. Distribusi relatif normal, namun terdapat sedikit rumah dengan jumlah kamar ekstrem (>6), yang menunjukkan variasi pada segmen properti skala besar.


- plot kamar mandi
> Rumah umumnya memiliki 1–2 kamar mandi. Outlier terjadi pada rumah dengan 5 atau lebih kamar mandi, yang kemungkinan merupakan properti mewah atau komersial.

- plot luas tanah
> Sebagian besar rumah memiliki luas tanah di bawah 200 m². Distribusi ini juga miring ke kanan, dengan outlier berupa rumah yang memiliki lahan sangat luas (>1000 m²). Ini mencerminkan adanya variasi tinggi pada segmen properti lahan besar yang perlu ditangani dalam modeling.

- plot luas bangunan
> Rumah umumnya memiliki luas bangunan antara 50 hingga 250 m². Beberapa properti dengan luas lebih dari 500 m² teridentifikasi sebagai outlier. Distribusi ini memperkuat pentingnya normalisasi atau transformasi saat pelatihan model prediktif.

- plot carports dan plot garasi
> Rumah pada umumnya memiliki 1 carport atau garasi. Properti dengan lebih dari 2 carport sangat jarang, menunjukkan bahwa fitur ini cukup spesifik untuk rumah mewah atau kavling besar.

- plot lantai
> Distribusi jumlah lantai menunjukkan bahwa mayoritas rumah adalah bertingkat 1 atau 2. Rumah dengan lebih dari 3 lantai sangat jarang, dan kemungkinan termasuk properti khusus seperti kos atau bangunan campuran.

- plot kamar ART dan plot kamar mandi ART
> Sebagian besar rumah tidak memiliki kamar khusus ART. Jika pun ada, jumlahnya 1 atau 2. Ini menunjukkan fitur ini lebih relevan untuk properti kelas atas.

- plot electicity
> Daya listrik rumah paling umum adalah antara 1.300 VA hingga 2.200 VA. Daya sangat tinggi (>4.400 VA) hanya dimiliki oleh sebagian kecil rumah, yang kemungkinan dilengkapi dengan fasilitas elektronik premium.

- plot umur bangunan
> Sebagian besar rumah berusia antara 0–20 tahun. Rumah dengan usia sangat tua (>40 tahun) sangat jarang dan dapat memengaruhi kondisi properti dan harga jualnya.

## **Fitur Kategorikal**
"""

categorical_cols = ['city', 'district', 'property_type', 'certificate',
                    'property_condition', 'furnishing']

for col in categorical_cols:
    plt.figure(figsize=(10, 4))
    sns.countplot(data=df_clean, x=col, order=df_clean[col].value_counts().index)
    plt.title(f'Distribusi Kategori: {col}')
    plt.xticks(rotation=45)
    plt.ylabel('Jumlah Properti')
    plt.show()

"""Insight

---
- plot kota
> Kota dengan jumlah properti terbanyak adalah Bekasi dan Tangerang, disusul oleh Depok dan Jakarta. Ini menunjukkan ekspansi pasar properti di wilayah penyangga Ibu Kota.

- plot distrik
> Sebaran wilayah memperlihatkan konsentrasi listing rumah pada wilayah pinggiran

- plot tipe
> hanya ada 1 variabel yaitu "rumah"

- plot sertifikat
> SHM (Sertifikat Hak Milik) merupakan sertifikat yang paling banyak ditemukan, menunjukkan legalitas properti yang kuat dan siap transaksi.

- plot kondisi
> Sebagian besar rumah dikategorikan dalam kondisi “Bagus”. Ini mencerminkan upaya pemilik atau agen untuk menampilkan properti dalam kondisi layak huni.

- plot furnishing
> Rumah unfurnished mendominasi iklan properti, disusul oleh semi-furnished. Furnished hanya sebagian kecil, biasanya ditujukan untuk apartemen atau rumah siap huni.

# **EDA Multivariate**

## **Korelasi matriks**
"""

plt.figure(figsize=(14, 10))
corr = df_clean.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", square=True, linewidths=0.5)
plt.title('Matriks Korelasi Fitur Numerik')
plt.show()

"""insight

---
Dari plot heatmap diatas dapat kita lihat ada hubungan erat antara 'price_in_rp' dengan 'building_size_m2' (0.49) dan ectricity (0.44). Dan juga antara 'building_size_m2' dengan 'electricity' (0.67) yang menunjukan bahwa makin besar sebuah bangunan, semakin besar juga listrik yang dibutuhkan

## **harga rata rata perkota**
"""

plt.figure(figsize=(10, 4))
avg_price_city = df_clean.groupby('city')['price_in_rp'].mean().sort_values(ascending=False)
sns.barplot(x=avg_price_city.index, y=avg_price_city.values)
plt.title('Harga Rata-rata Rumah per Kota')
plt.ylabel('Harga (Rp)')
plt.xticks(rotation=45)
plt.show()

"""Insight

---

Berdasarkan grafik harga rata-rata rumah per kota, terlihat bahwa Jakarta Pusat memiliki nilai properti tertinggi, disusul oleh Jakarta Selatan dan Jakarta Utara. Sementara itu, kota-kota satelit seperti Bekasi, Depok, dan Bogor memiliki rata-rata harga yang jauh lebih rendah, mengindikasikan bahwa kawasan tersebut menjadi pilihan utama bagi pembeli rumah dengan budget terbatas. Hal ini menegaskan adanya disparitas harga antar wilayah yang signifikan di Jabodetabek.

## **Harga rata rata berdasarkan kondisi properti**
"""

plt.figure(figsize=(8, 4))
avg_price_type = df_clean.groupby('property_condition')['price_in_rp'].mean().sort_values(ascending=False)
sns.barplot(x=avg_price_type.index, y=avg_price_type.values)
plt.title('Harga Rata-rata Berdasarkan Tipe Properti')
plt.ylabel('Harga (Rp)')
plt.xticks(rotation=45)
plt.show()

"""Insight

---

Dari plot diatas dapat kita lihat kalau harga rata-rata tertinggi dimiliki oleh properti yang membutuhkan renovasi. Hal ini mengindikasikan bahwa lokasi dan ukuran properti bisa jauh lebih menentukan harga dibandingkan kondisi fisik saat ini. Properti dalam kondisi “bagus sekali” dan “bagus” juga memiliki nilai tinggi, sejalan dengan ekspektasi. Sebaliknya, properti “baru”, “semi-furnished”, dan “unfurnished” memiliki harga rata-rata lebih rendah, kemungkinan besar karena berlokasi di kawasan dengan harga tanah lebih murah atau segmentasi pasar yang lebih rendah.

## **scatter ukuran vs harga**
"""

plt.figure(figsize=(10, 5))
sns.scatterplot(data=df_clean, x='land_size_m2', y='price_in_rp', hue='city')
plt.title('Luas Tanah vs Harga Rumah')
plt.xlabel('Luas Tanah (m2)')
plt.ylabel('Harga Rumah (Rp)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()

"""Insight

---

Grafik Luas Tanah vs Harga Rumah menunjukkan bahwa terdapat hubungan positif antara luas lahan dan harga rumah, meskipun tidak bersifat linier. Beberapa properti berharga tinggi meskipun memiliki lahan kecil, terutama di Jakarta Pusat dan Selatan, menandakan bahwa lokasi menjadi faktor dominan. Sebaliknya, rumah dengan luas tanah besar di wilayah seperti Bogor dan Tangerang cenderung memiliki harga yang lebih rendah. Hal ini mengindikasikan bahwa strategi prediksi harga rumah perlu mempertimbangkan interaksi antara ukuran fisik dan lokasi properti.

# Data Preparation

## **handling missing value**
"""

df_clean.isnull().sum()

"""karena missing value kolom 'building_age' dan 'building_orientation' lebih banyak jadi kita bisa melakukan drop kolom"""

# Drop kolom dengan missing value > 40%
df_clean.drop(columns=['building_age', 'building_orientation'], inplace=True)

"""dan juga untuk 'property_type' yang missing valuenya 1, kita juga bisa drop 1 baris yang memiliki missing value"""

# Drop baris dengan missing kecil
df_clean.dropna(subset=['property_type'], inplace=True)

"""kita bisa menggunakan median untuk kolom numerik yuang memiliki missing value"""

# Imputasi numerik dengan median
median_cols = ['bedrooms', 'bathrooms', 'land_size_m2', 'building_size_m2', 'floors', 'electricity']
for col in median_cols:
    df_clean[col].fillna(df_clean[col].median(), inplace=True)

"""sedangkan untuk kolom kategori, kita bisa menggunakan modus"""

# Imputasi kategorik dengan modus
mode_cols = ['certificate', 'property_condition', 'furnishing']
for col in mode_cols:
    df_clean[col].fillna(df_clean[col].mode()[0], inplace=True)

"""Mengapa kolom numerik menggunakan median dan ketegori menggunakan modus ?

Untuk menghindari kehilangan data berharga akibat penghapusan baris, serta menjaga distribusi agar tidak bias. Oleh karena itu kita menggunakan median dan modus
"""

df_clean.isnull().sum()

df_clean.head()

"""## **Eda Final**"""

plt.figure(figsize=(10, 5))
sns.histplot(df_clean['price_in_rp'], bins=50, kde=True)
plt.title('Distribusi Harga Rumah (Rp)')
plt.xlabel('Harga Rumah (Rp)')
plt.ylabel('Frekuensi')
plt.show()

# Log Transform
plt.figure(figsize=(10, 5))
sns.histplot(np.log1p(df_clean['price_in_rp']), bins=50, kde=True)
plt.title('Distribusi Harga Rumah (log1p Rp)')
plt.xlabel('Log Harga Rumah')
plt.ylabel('Frekuensi')
plt.show()

"""#**Feature Engineering**"""

# Buat kolom baru untuk harga log
df_clean['price_log'] = np.log1p(df_clean['price_in_rp'])

df_model = df_clean.copy()

# One-hot encoding
df_model = pd.get_dummies(df_model, columns=[
    'city', 'property_type', 'certificate',
    'furnishing', 'property_condition'
], drop_first=True)

df_model = df_model.drop(columns=[
    'price_in_rp', 'facilities', 'lat', 'long', 'district'
])

"""## Splitting

Untuk membuat model, kita membagi data menjadi 2 yaitu data training (80%) dan data testing (20%)
"""

X = df_model.drop(columns='price_log')
y = df_model['price_log']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

"""# Build Model

Untuk perbandingan, saya membuat model menggunakan 2 algoritma
- Linear Regression
- Random Forest

Mengapa menggunakan Linear Regression dan Random Forest ?
> Linear Regression digunakan sebagai baseline karena sederhana, cepat, dan mudah diinterpretasi

>Random Forest digunakan karena memiliki kelebihan, yaitu Akurat untuk data non-linear dan Tidak rentan overfitting
"""

lr = LinearRegression(
    fit_intercept=True,
    copy_X=True,
    n_jobs=None,
    positive=False
)
lr.fit(X_train, y_train)

rf = RandomForestRegressor(
    n_estimators=100,
    max_depth=None,
    min_samples_split=2,
    min_samples_leaf=1,
    max_features='sqrt',
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

"""# Eval"""

y_pred_lr = lr.predict(X_test)
rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
r2_lr = r2_score(y_test, y_pred_lr)

print(f"Linear Regression RMSE: {rmse_lr}")
print(f"Linear Regression R²: {r2_lr}")

y_pred_rf = rf.predict(X_test)
rmse_rf = np.sqrt(mean_squared_error(y_test, y_pred_rf))
r2_rf = r2_score(y_test, y_pred_rf)

print(f"Random Forest RMSE: {rmse_rf}")
print(f"Random Forest R²: {r2_rf}")

"""Insight

---

Bisa dilihat dari evaluasi diatas, hasil yang didapat adalah

| Model               | RMSE         | R² Score  |
|---------------------|--------------|-----------|
| Linear Regression   | 1.08e+09     | 0.6324    |
| Random Forest       | 7.01e+08     | 0.8043    |

Dari tabel diatas, dapat dibuktikan kalau Random Forest bagus untuk dijadikan alogirma model

## **Visualisasi**
"""

y_pred = rf.predict(X_test)

plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')  # Garis ideal
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Price (Random Forest)")
plt.grid(True)
plt.show()

residuals = y_test - y_pred

plt.figure(figsize=(8, 6))
sns.scatterplot(x=y_pred, y=residuals, alpha=0.6)
plt.axhline(0, color='red', linestyle='--')
plt.xlabel("Predicted Price")
plt.ylabel("Residuals")
plt.title("Residuals vs Predicted Price (Random Forest)")
plt.grid(True)
plt.show()

"""# Save Model"""

joblib.dump(rf, 'random_forest_model.pkl')

"""# Fitur Utama

## **Fungsi Prediksi**
"""

def predict_price(user_input: dict, model, feature_columns):
    df_input = pd.DataFrame([user_input])
    df_input = df_input[feature_columns]
    log_price = model.predict(df_input)[0]
    price = np.expm1(log_price)
    return round(price)

"""## **Fungsi Rekomendasi**"""

def recommend_houses(budget, df_original, top_n=5, tolerance=0.10):
    min_price = budget * (1 - tolerance)
    max_price = budget * (1 + tolerance)

    filtered = df_original[
        (df_original['price_in_rp'] >= min_price) &
        (df_original['price_in_rp'] <= max_price)
    ].sort_values(by='price_in_rp').head(top_n)

    return filtered[['district', 'city', 'bedrooms', 'bathrooms', 'land_size_m2',
                     'building_size_m2', 'price_in_rp', 'certificate', 'furnishing']]

"""## Model Testing

pada code ini saya akan mencoba testing, apakah model dapat merekomendasikan sesuai harga yang user input
"""

budget_user = input("Masukkan budget Anda (dalam Rupiah): ")

try:
  budget_user = int(budget_user)
  recommended_df = recommend_houses(budget_user, df_clean, top_n=5)
  print(f"\n📌 Rekomendasi Rumah Untuk Budget Rp {budget_user:,.0f}:\n")
  if not recommended_df.empty:
    print(recommended_df.to_string(index=False))
  else:
    print("Tidak ada rumah yang ditemukan dalam rentang budget Anda.")
except ValueError:
  print("Input tidak valid. Harap masukkan angka untuk budget.")

budget_user = input("Masukkan budget Anda (dalam Rupiah): ")

try:
  budget_user = int(budget_user)
  recommended_df = recommend_houses(budget_user, df_clean, top_n=5)
  print(f"\n📌 Rekomendasi Rumah Untuk Budget Rp {budget_user:,.0f}:\n")
  if not recommended_df.empty:
    print(recommended_df.to_string(index=False))
  else:
    print("Tidak ada rumah yang ditemukan dalam rentang budget Anda.")
except ValueError:
  print("Input tidak valid. Harap masukkan angka untuk budget.")