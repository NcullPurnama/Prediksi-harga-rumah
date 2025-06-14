# Analisis Prediktif Harga Rumah di Jabodetabek

## 📌 Latar Belakang

Ketersediaan hunian yang layak dengan harga terjangkau merupakan salah satu kebutuhan dasar masyarakat, terutama di kawasan perkotaan padat seperti Jabodetabek (Jakarta, Bogor, Depok, Tangerang, dan Bekasi). Wilayah ini merupakan pusat aktivitas ekonomi nasional dan mengalami pertumbuhan penduduk yang tinggi setiap tahunnya.

Namun demikian, harga rumah di Jabodetabek sangat bervariasi dan cenderung meningkat dari waktu ke waktu. Kenaikan ini dipengaruhi oleh berbagai faktor seperti lokasi, akses transportasi, ukuran lahan, fasilitas umum sekitar, serta legalitas properti. Situasi ini menciptakan tantangan bagi calon pembeli rumah, developer, hingga investor dalam menilai kewajaran harga sebuah properti.

Dalam konteks tersebut, pendekatan analitik berbasis data menjadi penting untuk membantu berbagai pihak memprediksi harga rumah secara lebih objektif, akurat, dan efisien. Salah satu pendekatan yang dapat digunakan adalah **Predictive Analytics**, yakni penerapan teknik statistik dan machine learning untuk memperkirakan nilai harga rumah berdasarkan data historis dan karakteristik properti.

---

## 🎯 Mengapa Masalah Ini Harus Diselesaikan?

1. **Membantu Akses Terhadap Hunian yang Terjangkau**  
   Menurut data **Badan Pusat Statistik (BPS)**, backlog (kekurangan) perumahan di Indonesia mencapai lebih dari **12 juta unit** (BPS, 2020). Prediksi harga yang akurat dapat membantu masyarakat dalam merencanakan pembelian rumah dengan lebih baik.

2. **Transparansi Pasar Properti**  
   Harga rumah yang ditentukan tanpa dasar data sering kali tidak mencerminkan nilai sebenarnya. Dengan prediksi berbasis data, pasar menjadi lebih transparan, adil, dan efisien.

3. **Pengambilan Keputusan oleh Developer dan Investor**  
   Developer memerlukan estimasi harga pasar untuk menentukan harga jual, sementara investor membutuhkan data harga untuk mengevaluasi potensi keuntungan investasi properti.

4. **Dukungan Bagi Sektor Keuangan dan Perbankan**  
   Lembaga keuangan seperti bank perlu menilai **nilai wajar properti** yang dijadikan agunan kredit pemilikan rumah (KPR). Prediksi harga berbasis data membantu proses ini menjadi lebih objektif.

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
   - AutoML (misalnya Auto-Sklearn)

4. **Evaluasi Kinerja Model**  
   Mengukur performa model menggunakan metrik seperti:
   - Mean Absolute Error (MAE)
   - Root Mean Square Error (RMSE)
   - R-Squared (R²)

5. **Implementasi dan Visualisasi**  
   Menyajikan hasil prediksi dalam bentuk grafik dan dashboard untuk membantu pengguna akhir memahami hasil secara visual.

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
   
   Kaggle Datasets.  
   [https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek](https://www.kaggle.com/datasets/nafisbarizki/daftar-harga-rumah-jabodetabek)

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

