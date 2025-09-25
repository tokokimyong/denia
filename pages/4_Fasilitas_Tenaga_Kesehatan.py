import streamlit as st
import pandas as pd

st.title("🏥 Fasilitas & Tenaga Kesehatan Terdekat")

st.subheader("Fasilitas Kesehatan (Contoh Data)")
data_faskes = {
    "Nama": ["RSUD Banyumas", "Puskesmas Purwokerto Timur", "Klinik Sehat Ibu"],
    "Alamat": ["Jl. Rumah Sakit No.1", "Jl. Jendral Sudirman No.45", "Jl. Diponegoro No.10"],
    "Telepon": ["0281-123456", "0281-654321", "0281-789012"]
}
df_faskes = pd.DataFrame(data_faskes)
st.table(df_faskes)

# Tombol untuk membuka Google Maps dengan query "faskes dekat saya"
st.markdown(
    """
    🔎 Ingin mencari lokasi terdekat?  
    [📍 Klik di sini untuk membuka Google Maps](https://www.google.com/maps/search/faskes+dekat+saya)
    """,
    unsafe_allow_html=True
)

st.subheader("Kontak Tenaga Kesehatan (Contoh)")
st.write("""
👩‍⚕️ **Bidan Ani** – 0812-3456-7890  
👨‍⚕️ **dr. Budi** – 0813-9876-5432  
☎️ **Hotline Anemia Ibu Hamil** – 1500-123
""")
