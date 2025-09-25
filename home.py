import streamlit as st
from PIL import Image

st.set_page_config(page_title="DENIA - Deteksi Dini Anemia", layout="centered")




# ===== Tampilkan Logo di Tengah =====
col1, col2, col3 = st.columns([1,2,1])
with col2:
    try:
        logo = Image.open("logo.png")
        st.image(logo, use_container_width=True)
    except:
        st.info("Tambahkan file logo.png di folder utama untuk menampilkan logo.")

# ===== Judul & Deskripsi =====
st.title("🌸 Aplikasi DENIA - Deteksi Dini Anemia")
st.markdown("""
Selamat datang di aplikasi ini.  
Aplikasi ini dirancang untuk membantu **deteksi dini anemia** pada ibu hamil,  
serta memberikan **informasi kesehatan** dan **akses ke fasilitas kesehatan** terdekat.
""")

# ===== Menu Utama =====
st.subheader("📌 Menu Utama")
st.write("Silakan pilih halaman melalui sidebar di kiri atau link di bawah:")

st.page_link("pages/1_Deteksi_Dini_Anemia.py", label="🩺 Deteksi Dini Anemia")
st.page_link("pages/2_Informasi_Anemia.py", label="📖 Informasi Anemia")
st.page_link("pages/3_Kuesioner_Prediksi_Anemia.py", label="✍️ Kuesioner Prediksi Anemia")
st.page_link("pages/4_Fasilitas_Tenaga_Kesehatan.py", label="🏥 Fasilitas & Tenaga Kesehatan")

