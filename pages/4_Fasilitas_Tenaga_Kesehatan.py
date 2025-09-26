import streamlit as st
import pandas as pd
import urllib.parse

st.title("🏥 Fasilitas & Tenaga Kesehatan Terdekat")

# -----------------------------
# Bagian 1: Skema Layanan
# -----------------------------
st.subheader("🔄 Alur Konsultasi")
st.markdown(
    """
    1️⃣ **Chatbot AI (DENIA)** → Jawab pertanyaan ringan & edukasi dasar.  
    2️⃣ **Tenaga Kesehatan** → Jika pertanyaan serius atau butuh interaksi langsung, diarahkan ke bidan/dokter.  
    3️⃣ **Fasilitas Kesehatan** → Jika gawat darurat, segera menuju RS/Puskesmas terdekat.  
    """
)

# -----------------------------
# Bagian 2: Akses Chatbot AI
# -----------------------------
st.subheader("🤖 Chat dengan DENIA (AI)")
st.markdown(
    """
    Klik tombol di bawah untuk membuka chatbot AI.  
    (Catatan: jawaban AI hanya untuk edukasi, **bukan pengganti diagnosis tenaga kesehatan**.)
    """
)

st.page_link("pages/5_chatbotai.py", label="💬 Buka Chatbot AI")


# -----------------------------
# Bagian 3: Kontak Tenaga Kesehatan
# -----------------------------
st.subheader("👩‍⚕️ Kontak Tenaga Kesehatan")

nakes = [
    {"nama": "👩‍⚕️ Bidan Ani", "wa": "6281327717444"},
    {"nama": "👨‍⚕️ dr. Budi", "wa": "6281398765432"},
]

if "identitas" in st.session_state:
    identitas = st.session_state["identitas"]
    pesan = f"Halo, saya {identitas.get('nama','')}, umur {identitas.get('umur','')} tahun, alamat {identitas.get('alamat','')}, kehamilan {identitas.get('kehamilan','')}."
    pesan_encoded = urllib.parse.quote_plus(pesan)

    for n in nakes:
        wa_url = f"https://wa.me/{n['wa']}?text={pesan_encoded}"
        st.markdown(
            f'''
            <a href="{wa_url}" target="_blank" rel="noopener noreferrer"
               style="text-decoration:none">
               <div style="display:inline-block; margin:6px;">
                 <button style="
                   background-color:#25D366;
                   color:white;
                   padding:8px 12px;
                   border-radius:8px;
                   border:none;
                   font-weight:600;
                   cursor:pointer;
                 ">
                   💬 Chat via WhatsApp {n["nama"]}
                 </button>
               </div>
            </a>
            ''',
            unsafe_allow_html=True
        )
else:
    st.info("⚠️ Silakan isi identitas diri di halaman depan sebelum menghubungi tenaga kesehatan.")

# -----------------------------
# Bagian 4: Fasilitas Kesehatan
# -----------------------------
st.subheader("🏥 Fasilitas Kesehatan (Contoh Data)")
data_faskes = {
    "Nama": ["RSUD Banyumas", "Puskesmas Purwokerto Timur", "Klinik Sehat Ibu"],
    "Alamat": ["Jl. Rumah Sakit No.1", "Jl. Jendral Sudirman No.45", "Jl. Diponegoro No.10"],
    "Telepon": ["0281-123456", "0281-654321", "0281-789012"]
}
df_faskes = pd.DataFrame(data_faskes)
st.table(df_faskes)

st.markdown(
    """
    🔎 Ingin mencari lokasi terdekat?  
    [📍 Klik di sini untuk membuka Google Maps](https://www.google.com/maps/search/faskes+dekat+saya)
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Bagian 5: Hotline
# -----------------------------
st.subheader("☎️ Hotline")
st.write("📞 **Hotline Anemia Ibu Hamil** – 1500-123")
