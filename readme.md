# Prediksi Harga Rumah di California

Aplikasi ini memungkinkan pengguna untuk memprediksi harga rumah di California berdasarkan beberapa faktor seperti pendapatan, umur rumah, jumlah kamar, dan lokasi geografis.

## Fitur Aplikasi:
- Memasukkan data pengguna melalui input berupa slider untuk berbagai fitur.
- Menggunakan model **CatBoostRegressor** yang telah dilatih untuk memprediksi harga rumah berdasarkan data yang diberikan.
- Menampilkan hasil prediksi harga rumah di California.

## Prasyarat

Untuk menjalankan aplikasi ini, Anda perlu mengatur lingkungan pengembangan menggunakan **Conda** dan menginstal pustaka yang diperlukan.

### 1. **Menggunakan Conda untuk Mengaktifkan Lingkungan Virtual**

Jika Anda menggunakan Conda, pertama-tama buat dan aktifkan lingkungan virtual untuk proyek ini dengan perintah berikut:

```bash
conda create -n streamlit-env python=3.10.16
conda activate streamlit-env

### 2. **Instal Pustaka yang Diperlukan**

```bash
cd C:\Users\Lenovo\OneDrive\Documents\California_Housing
pip install pipreqs
pipreqs . --force
pip install -r requirements.txt

### 3. **Jalankan Aplikasi**

``` bash
streamlit dashboard.py


### 4. **Struktur Proyek

``` bash
California_Housing/
│
├── California Housing .jpg     # Gambar Ilustrasi california house
├── california_housing.csv      # Dataset untuk moodel
├── catboost_model.cbm          # MModel yang telah dilatih
├── readme.md                   # Berkas menjalankan dashboard.py
└── requirements.txt            # Daftar pustaka yang dibutuhkan untuk proyek

Ini adalah **readme.md** yang lengkap dengan instruksi langkah-demi-langkah yang mencakup penginstalan **`pipreqs`**, pembuatan file **`requirements.txt`**, dan cara menjalankan aplikasi. Anda dapat menambahkan atau menyesuaikan bagian lainnya sesuai kebutuhan proyek Anda.
