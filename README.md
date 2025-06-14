# Analisis Prediktif Harga Rumah di Jabodetabek

## 📌 Latar Belakang

Harga rumah di wilayah Jabodetabek terus meningkat seiring dengan meningkatnya kebutuhan tempat tinggal dan pertumbuhan penduduk. Bagi calon pembeli, investor, dan pengembang properti, memprediksi harga rumah secara akurat sangat penting agar dapat mengambil keputusan yang lebih tepat.

Menurut Property Market Outlook 2024 oleh Colliers, pasar residensial di Jabodetabek menunjukkan pertumbuhan yang konsisten dengan adanya permintaan dari segmen menengah ke bawah. Data dari Rumah123 juga menunjukkan tren kenaikan harga rumah tahunan sekitar 10–15% di wilayah ini.

Dalam konteks tersebut, pendekatan analitik berbasis data menjadi penting untuk membantu berbagai pihak memprediksi harga rumah secara lebih objektif, akurat, dan efisien. Salah satu pendekatan yang dapat digunakan adalah **Predictive Analytics**, yakni penerapan teknik statistik dan machine learning untuk memperkirakan nilai harga rumah berdasarkan data historis dan karakteristik properti.

---

## 🎯 Mengapa Masalah Ini Harus Diselesaikan?

1. Bagaimana memprediksi harga rumah berdasarkan fitur-fitur seperti lokasi, ukuran tanah, jumlah kamar, dan lainnya?

2. Algoritma machine learning mana yang memberikan akurasi terbaik untuk masalah ini?

---

##🎯 Goals

1. Menghasilkan model prediksi harga rumah yang akurat dan dapat digunakan untuk membantu proses pengambilan keputusan.

2. Mengevaluasi performa beberapa algoritma dan memilih model terbaik berdasarkan metrik RMSE dan R².

---
## 🛠️ Bagaimana Masalah Ini Diselesaikan?

Masalah prediksi harga rumah dapat diselesaikan melalui pendekatan **Predictive Analytics berbasis Machine Learning**, dengan langkah-langkah sebagai berikut:

1. **Pengumpulan dan Eksplorasi Data**  
   Menggunakan dataset yang berisi informasi tentang harga rumah dan fitur-fiturnya, seperti yang disediakan oleh Nafis Barizki (2022) melalui Kaggle:  
   [Daftar Harga Rumah Jabodetabek – Kaggle](https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek)

2. **Pra-Pemrosesan Data**  
   Membersihkan data, mengatasi nilai kosong, melakukan encoding pada variabel kategorikal, dan menormalisasi data numerik.

3. **Pemilihan Model Machine Learning**  
   Menggunakan algoritma prediktif seperti:
   - Linear Regression
   - Random Forest
   - XGBoost

4. **Evaluasi Kinerja Model**  
   Mengukur performa model menggunakan metrik seperti:
   - Mean Absolute Error (MAE)
   - Root Mean Square Error (RMSE)
   - R-Squared (R²)

5. **Implementasi dan Visualisasi**  
   Menyajikan hasil prediksi dalam bentuk grafik dan dashboard untuk membantu pengguna akhir memahami hasil secara visual.

---

## 💡 Solution Statements

Untuk mencapai tujuan prediksi harga rumah secara akurat, solusi yang diimplementasikan dalam proyek ini adalah sebagai berikut:

### ✅ **Solusi 1: Linear Regression sebagai Baseline**
- **Deskripsi**: Linear Regression dipilih sebagai model baseline karena merupakan metode yang sederhana dan mampu menangkap hubungan linier antara fitur-fitur seperti luas bangunan, jumlah kamar, dan lokasi dengan harga rumah.
- **Evaluasi**:
  - **Mean Squared Error (MSE)**
  - **Root Mean Squared Error (RMSE)**
  - **R² Score (koefisien determinasi)**
- **Peran**: Model ini berfungsi sebagai pembanding untuk mengevaluasi apakah model yang lebih kompleks dapat memberikan peningkatan akurasi yang signifikan.

---

### ✅ **Solusi 2: Random Forest Regressor untuk Model Non-Linear**
- **Deskripsi**: Random Forest dipilih karena mampu menangani data non-linear dan dapat memanfaatkan interaksi antar fitur secara otomatis. Algoritma ini bekerja dengan membentuk banyak pohon keputusan (decision trees) dan menggabungkan hasil prediksi mereka.
- **Evaluasi**:
  - **MSE**, **RMSE**, dan **R² Score** dibandingkan dengan model Linear Regression
  - Menggunakan `train_test_split` untuk menguji performa model pada data testing
- **Perbaikan (Improvement)**:
  - Menyesuaikan parameter seperti `n_estimators`, `max_depth`, dan `min_samples_split` untuk meningkatkan akurasi prediksi

---

Setiap model dievaluasi secara objektif berdasarkan metrik akurasi prediksi dan dipilih model dengan performa terbaik untuk dijadikan sistem rekomendasi harga rumah.

---

## 📊 Dataset Overview

### 🔗 Sumber Data

Dataset yang digunakan berasal dari situs **Kaggle**, yaitu:

> **Daftar Harga Rumah Jabodetabek**  
> Link: [https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek](https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek)

Dataset ini dikumpulkan dari listing properti pada website jual-beli rumah, dan berisi informasi lengkap mengenai atribut rumah di wilayah Jakarta, Bogor, Depok, Tangerang, dan Bekasi (Jabodetabek).

---

### 📦 Informasi Dataset

- **Jumlah baris (entri):** 3553
- **Jumlah kolom (fitur):** 27
- **Tipe data:** kombinasi antara numerik (`float64`) dan kategorikal (`object`)
- **Kondisi data:** terdapat beberapa nilai kosong (missing values) terutama pada fitur `building_age`, `property_condition`, `furnishing`, dan `building_orientation`

---

### 🏷️ Fitur/Variabel pada Dataset

| Nama Kolom              | Deskripsi                                                                 |
|-------------------------|--------------------------------------------------------------------------|
| `url`                   | URL iklan rumah                                                          |
| `price_in_rp`           | Harga rumah dalam Rupiah                                                 |
| `title`                 | Judul iklan rumah                                                        |
| `address`               | Alamat properti                                                          |
| `district`              | Nama kecamatan atau area                                                 |
| `city`                  | Nama kota                                                                |
| `lat`, `long`           | Lokasi geografis properti (latitude dan longitude)                      |
| `facilities`            | Fasilitas yang tersedia (misalnya taman, masjid, dll)                    |
| `property_type`         | Jenis properti (rumah, apartemen, dll)                                  |
| `ads_id`                | ID iklan                                                                 |
| `bedrooms`              | Jumlah kamar tidur                                                       |
| `bathrooms`             | Jumlah kamar mandi                                                       |
| `land_size_m2`          | Luas tanah dalam meter persegi                                           |
| `building_size_m2`      | Luas bangunan dalam meter persegi                                        |
| `carports`              | Jumlah carport                                                           |
| `certificate`           | Jenis sertifikat (SHM, HGB, dll)                                         |
| `electricity`           | Daya listrik rumah                                                       |
| `maid_bedrooms`         | Jumlah kamar ART                                                         |
| `maid_bathrooms`        | Jumlah kamar mandi ART                                                   |
| `floors`                | Jumlah lantai                                                            |
| `building_age`          | Usia bangunan                                                            |
| `year_built`            | Tahun dibangun                                                           |
| `property_condition`    | Kondisi bangunan (bagus, sedang, dll)                                    |
| `building_orientation`  | Arah bangunan menghadap                                                  |
| `garages`               | Jumlah garasi                                                            |
| `furnishing`            | Status kelengkapan (furnished/unfurnished/semi)                          |

---

## 🧪 Exploratory Data Analysis (EDA)

### 1. Statistik Umum

Dataset terdiri dari:
- Harga rumah: dari **ratusan juta hingga puluhan miliar**
- Luas tanah: bervariasi dari kecil (30m²) hingga sangat luas (>1000m²)
- Jumlah kamar tidur & mandi: rentang 1–10+
- Daya listrik: berkisar antara 900 VA hingga 6600 VA ke atas

### 2. Visualisasi dan Distribusi Awal

Beberapa langkah EDA yang dilakukan:
- **Distribusi harga** (`price_in_rp`) dengan histogram → data bersifat **right-skewed**
- **Korelasi numerik** antar fitur (`land_size_m2`, `building_size_m2`, `bedrooms`) terhadap harga rumah
- **Boxplot** untuk melihat penyebaran harga per `city` dan `property_type`
- **Heatmap korelasi** antar fitur numerik → mengungkap fitur paling relevan terhadap `price_in_rp`

---

EDA ini membantu memahami pola dan variabel yang paling berkontribusi dalam menentukan harga rumah serta mendeteksi outlier atau missing value yang perlu ditangani sebelum modeling.

---

## 📈 Visualisasi Distribusi Fitur Numerik

### Distribusi Luas Tanah
![Distribusi Luas Tanah](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_luas_tanah.png)

### Distribusi Luas Bangunan
![Distribusi Luas Bangunan](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_luas_bangunan.png)

### Distribusi Jumlah Lantai
![Distribusi Lantai](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_lantai.png)

### Distribusi Listrik
![Distribusi Listrik](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_listrik.png)

### Distribusi Carport
![Distribusi Carport](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_carport.png)

### Distribusi Garasi
![Distribusi Garasi](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_garasi.png)

### Distribusi Jumlah Kamar
![Distribusi Kamar](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kamar.png)

### Distribusi Jumlah Kamar Mandi
![Distribusi Kamar Mandi](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kamar_mandi.png)

### Distribusi Kamar ART
![Distribusi Kamar ART](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kamar_ART.png)

### Distribusi Harga Rumah
![Distribusi Harga Rumah](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_harga_rumah.png)

---

## Visualisasi Distribusi Fitur Kategorikal

### Tipe Furnishing
![Distribusi Furnishing](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kategori_furnishing.png)

### Kondisi Properti
![Distribusi Kondisi Properti](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kategori_kondisi.png)

### Kota
![Distribusi Kota](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kategori_kota.png)

### Sertifikat
![Distribusi Sertifikat](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kategori_sertifikat.png)

### Tipe Properti
![Distribusi Tipe Properti](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kategori_tipe.png)

### Wilayah
![Distribusi Wilayah](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/distribusi_kategori_wilayah.png)

---

## Heatmap Korelasi

### Korelasi Antar Variabel Numerik
![Heatmap Korelasi](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/heatmap.png)


---

## 🧹 Data Preparation

Proses data preparation bertujuan untuk membersihkan dan menyiapkan data agar dapat digunakan oleh model machine learning secara optimal. Berikut adalah tahapan yang dilakukan secara berurutan:

---

### 1. Menghapus Kolom Tidak Relevan
Beberapa kolom seperti `url`, `title`, `address`, `ads_id`, `year_built`, `building_age`, dan `building_orientation` dihapus karena:
- Tidak berkontribusi langsung terhadap prediksi harga.
- Bersifat unik atau teks bebas yang sulit diolah tanpa NLP khusus.

![kolom tidak relevan](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/tidak_relevan.jpg)

> 📌 **Alasan:** Kolom tersebut dapat menambah noise dalam data dan meningkatkan kompleksitas model tanpa manfaat yang signifikan.

---

### 2. Menangani Missing Values
Beberapa kolom dengan missing values diisi sebagai berikut:

- Kolom numerik seperti `bedrooms`, `bathrooms`, `land_size_m2`, `building_size_m2`, `floors`, `carports` diisi dengan median
- Kolom kategorikal seperti `certificate`, `property_condition`, dan `furnishing` diisi dengan modus

Teknik yang digunakan:
- Untuk numerik: diisi dengan **median**
- Untuk kategorikal: diisi dengan **modus (nilai paling sering)**

![median](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/median.jpg)
![modus](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/modus.jpg)

> 📌 **Alasan:** Menghindari kehilangan data berharga akibat penghapusan baris, serta menjaga distribusi agar tidak bias.

---

### 3. Encoding Variabel Kategorikal 
Kolom seperti `city`, `property_type`, `certificate`, `furnishing`, dan `building_orientation` diubah menjadi numerik menggunakan:
**One-Hot Encoding** (pd.get_dummies())

![One Hot](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/one-hot.jpg)

> 📌 **Alasan:** Model machine learning tidak dapat memproses data string secara langsung. Encoding memungkinkan model memahami informasi kategorikal.

---

### 4. Membagi Dataset
Dataset dibagi menjadi:
- **Training Set (80%)**
- **Testing Set (20%)**

Menggunakan `train_test_split` dari `sklearn.model_selection` dengan parameter `random_state` agar hasil replikasi konsisten.

![membagi dataset](https://raw.githubusercontent.com/NcullPurnama/Prediksi-harga-rumah/main/gambar/membagi.jpg)

> 📌 **Alasan:** Pembagian ini penting untuk mengukur performa model terhadap data yang tidak dilatih.

---

Dengan urutan preprocessing di atas, dataset menjadi bersih, konsisten, dan siap digunakan untuk pelatihan model prediktif.
---

## 🤖 Machine Learning Modeling

Untuk menyelesaikan permasalahan prediksi harga rumah di wilayah Jabodetabek, dua algoritma digunakan dan dibandingkan, yaitu:

1. **Linear Regression** sebagai baseline model
2. **Random Forest Regressor** sebagai model yang mampu menangkap relasi non-linear

---

### 🔍 Tahapan dan Parameter Model

#### 1. Linear Regression
- **Library**: `sklearn.linear_model.LinearRegression`
- **Parameter utama**:
  - `fit_intercept=True`: Menyertakan intercept dalam model.
  - `normalize=False`: Data sudah diskalakan sebelumnya, jadi tidak dilakukan normalisasi ulang.
- **Cara Kerja**: Model ini mempelajari hubungan linier antara fitur dan target.
> Digunakan sebagai baseline karena sederhana, cepat, dan mudah diinterpretasi.

#### 2. Random Forest Regressor
- **Library**: `sklearn.ensemble.RandomForestRegressor`
- **Parameter awal (default)**:
  - n_estimators=100 (Jumlah pohon dalam hutan. Semakin banyak pohon, semakin stabil prediksi (namun lebih lambat))
  - max_depth=None (Tidak ada batasan kedalaman pohon, memungkinkan model menyesuaikan secara bebas. Bisa meningkatkan akurasi model)
  - min_samples_split=2(Jumlah minimal sampel untuk membagi node internal. Nilai kecil memberi model lebih banyak fleksibilitas)
  - min_samples_leaf=1 (Jumlah minimal sampel pada daun pohon. Nilai kecil dapat membuat model sangat kompleks)
  - max_features='auto' (Menggunakan semua fitur pada regresi)
  - random_state=42 (Agar hasil yang didapat konsisten dan dapat direproduksi)
    
- **Cara Kerja**:
  - Model ensembel dari banyak decision tree
  - Mengambil rata-rata prediksi dari banyak pohon untuk menghasilkan prediksi akhir
  - Mampu menangani relasi non-linear dan data dengan banyak fitur kategorikal/numerik

---

### ⚖️ Kelebihan dan Kekurangan Algoritma

| Algoritma               | Kelebihan                                                                 | Kekurangan                                                              |
|------------------------|---------------------------------------------------------------------------|-------------------------------------------------------------------------|
| **Linear Regression**   | - Cepat dan efisien<br>- Mudah diinterpretasi                             | - Tidak mampu menangani relasi non-linear<br>- Rentan terhadap outlier |
| **Random Forest**       | - Akurat untuk data non-linear<br>- Tidak rentan overfitting              | - Lebih lambat dari linear regression<br>- Sulit diinterpretasi secara langsung |

---

### 🏆 Pemilihan Model Terbaik

#### 📈 Evaluasi Model

| Model               | MSE (lebih kecil lebih baik) | RMSE | R² Score (lebih tinggi lebih baik) |
|--------------------|------------------------------|------|-------------------------------------|
| Linear Regression  | 1.17e+18   | 1.08e+09           | 0.6324           |
| Random Forest      |  4.92e+17    | 7.01e+08 | 0.8043     |

> **Random Forest Regressor dipilih sebagai model terbaik** karena menghasilkan nilai R² dan RMSE yang jauh lebih baik dibandingkan baseline Linear Regression.

---

### ✅ Kesimpulan Pemodelan

Random Forest mampu menangkap kompleksitas hubungan antara fitur (jumlah kamar, luas bangunan, lokasi, dll.) dengan harga rumah. Oleh karena itu, model ini dipilih untuk menghasilkan rekomendasi harga rumah yang lebih akurat.

## 📏 Model Evaluation

Evaluasi model dilakukan untuk mengetahui seberapa baik model memprediksi harga rumah dibandingkan nilai sebenarnya. Dalam proyek ini, digunakan tiga metrik evaluasi regresi yang relevan:

---

### 📊 Metrik Evaluasi yang Digunakan

1. ### Mean Squared Error (**MSE**)
   - **Penjelasan**: Mengukur rata-rata kesalahan kuadrat antara nilai aktual \( y_i \) dan prediksi \( \hat{y}_i \). Semakin kecil MSE, semakin akurat model.
   - **Kelebihan**: Memberi penalti besar terhadap kesalahan besar (outlier).
   - **Kekurangan**: Tidak berada dalam satuan yang sama dengan target (Rp), karena dikuadratkan.

---

2. ### Root Mean Squared Error (**RMSE**)
   - **Penjelasan**: Akar dari MSE yang mengembalikan kesalahan dalam satuan asli (Rupiah), sehingga lebih mudah diinterpretasikan.
   - **Kelebihan**: Memberikan gambaran langsung tentang rata-rata deviasi prediksi dari harga sebenarnya.
   - **Interpretasi**: Jika RMSE = 500 juta, artinya prediksi rata-rata bisa meleset sebesar ±500 juta.

---

3. ### R² Score (Koefisien Determinasi)
   - **Penjelasan**: Mengukur proporsi variansi harga rumah yang bisa dijelaskan oleh model. Nilai berkisar antara 0 dan 1.
   - **Interpretasi**:
     - R² = 0.90 → 90% variasi harga rumah berhasil dijelaskan oleh fitur.
     - R² mendekati 1 berarti model sangat baik.

---

### 🧾 Hasil Evaluasi Model

| Model               | MSE              | RMSE             | R² Score         |
|--------------------|------------------|------------------|------------------|
| Linear Regression  | ✅ 1.17e+18 (lebih rendah)   | 1.08e+09           | 0.6324           |
| Random Forest      |  4.92e+17    | ✅ 7.01e+08 (lebih kecil)    | ✅ 0.8043 (mendekati 1)    |

> 🔍 Berdasarkan ketiga metrik tersebut, **Random Forest Regressor** terbukti memiliki performa yang lebih baik dalam memprediksi harga rumah.

---

### 🧠 Kesimpulan

Metrik evaluasi yang digunakan sudah sesuai dengan konteks **prediksi harga numerik** (regresi), dan model terbaik (Random Forest) memiliki:
- RMSE lebih rendah: 701 juta
- R² Score lebih tinggi: 0.8043

Evaluasi ini menunjukkan bahwa model bisa diandalkan untuk memberikan estimasi harga rumah yang masuk akal, khususnya untuk aplikasi rekomendasi.

---

## 📚 Referensi

1. **Badan Pusat Statistik (BPS). (2020).**  
   _“Statistik Perumahan dan Permukiman.”_ Jakarta: BPS.  
   > "Backlog perumahan di Indonesia mencapai lebih dari 12 juta unit."

2. **Nurfadillah, R., & Prasetyo, E. (2021).**  
   _“Prediksi Harga Rumah Menggunakan Metode Regresi dan Random Forest.”_  
   Jurnal Ilmiah Komputer dan Informatika (JIKI), Vol. 6 No. 2.  
   > Dalam studi ini, Random Forest terbukti lebih akurat dibandingkan metode regresi biasa untuk prediksi harga rumah.

3. **Huang, X., & Wong, M. S. (2020).**  
   _“Modeling Housing Price Using Machine Learning Algorithms: A Case Study of Hong Kong.”_  
   ISPRS International Journal of Geo-Information, 9(7), 423.  
   [https://doi.org/10.3390/ijgi9070423](https://doi.org/10.3390/ijgi9070423)  
   > Penelitian ini menyimpulkan bahwa Gradient Boosting dan Random Forest mampu memberikan akurasi tinggi dalam prediksi harga properti.

4. **Barizki, Nafis. (2022).**  
   _“Daftar Harga Rumah Jabodetabek.”_
   Kaggle Datasets.   [https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek](https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek)
