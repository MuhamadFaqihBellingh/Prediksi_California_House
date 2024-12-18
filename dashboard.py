import streamlit as st
import pandas as pd
from catboost import CatBoostRegressor, Pool
import numpy as np
import requests
import tempfile

# Set the page config to improve the visual layout
st.set_page_config(page_title="Prediksi Harga Rumah California", layout="wide")

# Menampilkan judul yang menarik
st.title('✨ Prediksi Harga Rumah di California')

# Menampilkan gambar ilustrasi rumah dengan caption yang menarik
st.image("https://github.com/MuhamadFaqihBellingh/Prediksi_California_House/blob/main/California%20Housing.jpg?raw=true", caption="Ilustrasi Rumah di California", use_container_width=True)

# Menambahkan deskripsi yang lebih informatif dengan desain yang bersih
st.markdown("""
## Deskripsi Dataset dan Cara Menggunakan
Aplikasi ini memungkinkan Anda untuk memprediksi harga rumah di California berdasarkan beberapa faktor. Masukkan data yang sesuai di bawah ini untuk mendapatkan perkiraan harga rumah.

**Fitur-fitur input** yang akan Anda masukkan meliputi:
- **Pendapatan per Kapita** (MedInc)
- **Umur Rumah** (HouseAge)
- **Rata-rata Kamar Tidur per Rumah** (AveRooms)
- dan banyak lagi...

Gunakan slider atau kolom angka untuk mengisi data. Setelah itu, klik "Prediksi Harga" dan lihat hasil estimasi harga rumah berdasarkan data yang Anda masukkan.
""")

# Input untuk data pengguna dengan slider dan deskripsi tambahan
st.subheader("Masukkan Data untuk Prediksi Harga Rumah")
MedInc = st.slider('Median Income (Pendapatan per Kapita)', 0.0, 20.0, 3.0)
HouseAge = st.slider('House Age (Umur Rumah)', 0, 100, 20)
AveRooms = st.slider('Average Rooms (Rata-rata Jumlah Kamar)', 0.0, 10.0, 5.0)
AveBedrms = st.slider('Average Bedrooms (Rata-rata Jumlah Kamar Tidur)', 0.0, 10.0, 3.0)
Population = st.slider('Population (Jumlah Penduduk)', 0, 50000, 1000)
AveOccup = st.slider('Average Occupancy (Rata-rata Penghuni per Rumah)', 0.0, 10.0, 3.0)
Latitude = st.slider('Latitude (Garis Lintang)', 32.0, 42.0, 37.0)
Longitude = st.slider('Longitude (Garis Bujur)', -125.0, -113.0, -119.0)

# Membuat DataFrame dari input pengguna
user_input = pd.DataFrame({
    'MedInc': [MedInc],
    'HouseAge': [HouseAge],
    'AveRooms': [AveRooms],
    'AveBedrms': [AveBedrms],
    'Population': [Population],
    'AveOccup': [AveOccup],
    'Latitude': [Latitude],
    'Longitude': [Longitude]
})

# Menampilkan data yang dimasukkan pengguna
st.write("Data yang Anda Masukkan:")
st.write(user_input)

# Tombol untuk menjalankan prediksi
if st.button("Prediksi Harga Rumah"):
    # Load model CatBoost yang telah dilatih
    cat_model_loaded = CatBoostRegressor()
    # URL model di GitHub
model_url = 'https://raw.githubusercontent.com/MuhamadFaqihBellingh/Prediksi_California_House/main/catboost_model.cbm'

# Mengunduh file model
response = requests.get(model_url)
if response.status_code == 200:
    # Simpan file sementara
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(response.content)
        model_path = tmp_file.name

    # Muat model dari file sementara
    cat_model_loaded = CatBoostRegressor()
    cat_model_loaded.load_model(model_path)
    st.write("Model berhasil dimuat.")
else:
    st.write("Gagal mengunduh model.")

    # Membuat Pool dari input pengguna
    user_input_pool = Pool(user_input)

    # Prediksi harga rumah menggunakan model yang telah dilatih
    predicted_price = cat_model_loaded.predict(user_input_pool)

    # Menampilkan hasil prediksi harga rumah
    st.subheader("Hasil Prediksi Harga Rumah")
    st.write(f"Prediksi harga rumah berdasarkan data yang Anda masukkan adalah sekitar **${predicted_price[0]:,.2f}**.")

    # Menambahkan sedikit penjelasan tentang hasil prediksi
    st.markdown("""
    **Penjelasan**: 
    Harga yang diprediksi berdasarkan data yang Anda masukkan menunjukkan estimasi harga rumah di wilayah California berdasarkan faktor-faktor seperti pendapatan, umur rumah, jumlah kamar, dan lainnya.
    """)

# Menambahkan pemberitahuan terkait kesalahan model
st.markdown("""
> **Peringatan:** Model yang digunakan mungkin masih mengandung kesalahan atau belum sepenuhnya valid. 
> Performa model ini dapat dipengaruhi oleh berbagai faktor, termasuk data yang tidak lengkap atau fitur yang tidak sepenuhnya mencerminkan kondisi pasar real estate di California.
> Harap diingat bahwa ini hanya perkiraan, dan hasil prediksi bisa saja tidak akurat.
""")
    
 # Footer dengan informasi aplikasi
st.markdown("""
    ---
    **Aplikasi oleh**: Muhamad Faqih   
    **Referensi Data**: [California Housing Dataset](https://archive.ics.uci.edu/ml/machine-learning-databases/00210/)
    """)
