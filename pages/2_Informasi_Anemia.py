import streamlit as st

st.title("📖 Informasi Anemia pada Ibu Hamil")

with st.expander("Definisi"):
    st.write("Anemia adalah kondisi ketika jumlah sel darah merah atau kadar hemoglobin (Hb) lebih rendah dari normal...\n- Normal: Hb ≥ 11 g/dL \n- Anemia ringan: Hb 10,0 – 10,9 g/dL \n- Anemia sedang: Hb 7,0 – 9,9 g/dL \n- Anemia berat: Hb < 7,0 g/dL")

with st.expander("Penyebab"):
    st.write("- Kekurangan zat besi\n- Kekurangan asam folat\n- Kekurangan vitamin B12\n- Kehilangan darah")

with st.expander("Dampak"):
    st.write(
        "**Pada Ibu:**\n"
        "- Mudah lelah, lemah, pusing, sesak\n"
        "- Risiko perdarahan saat persalinan lebih tinggi\n"
        "- Infeksi lebih mudah terjadi\n"
        "- Syok lebih berbahaya karena cadangan Hb sedikit\n"
        "- Risiko kematian ibu meningkat\n\n"
        "**Pada Janin:**\n"
        "- Gangguan pertumbuhan janin (IUGR → bayi lahir kecil/BBLR)\n"
        "- Kelahiran prematur\n"
        "- Asfiksia neonatorum (bayi lahir lemas)\n"
        "- Keguguran atau kematian janin dalam kandungan (IUFD)\n"
        "- Risiko bayi lahir dengan cadangan zat besi rendah\n\n"
        "**Dampak Jangka Panjang:**\n"
        "- Pada anak: gangguan tumbuh kembang, termasuk otak dan kognitif\n"
        "- Pada ibu: memperburuk penyakit kronis bila ada (misalnya jantung atau ginjal)"
    )

with st.expander("Tanda & Gejala"):
    st.write("- Lemas, lesu\n- Pucat\n- Sering pusing\n- Sesak nafas\n- Jantung berdebar")

with st.expander("Pencegahan"):
    st.write(
        "- **Konsumsi makanan bergizi seimbang:** sayuran hijau, kacang-kacangan, daging merah, hati, ikan, telur.\n"
        "- **Konsumsi vitamin C:** jeruk, tomat, jambu, agar penyerapan zat besi optimal.\n"
        "- **Hindari minuman penghambat zat besi:** teh, kopi, soda, terutama saat makan/minum tablet Fe.\n"
        "- **Rutin konsumsi tablet tambah darah (Fe):** sesuai anjuran tenaga kesehatan.\n"
        "- **Periksa kadar Hb secara berkala.**\n"
        "- **Jaga kebersihan diri & lingkungan:** mencegah cacingan.\n"
        "- **Atur jarak kehamilan:** beri waktu tubuh memulihkan cadangan zat besi."
    )

with st.expander("Penatalaksanaan"):
    st.write(
        "- **Anemia ringan–sedang:**\n"
        "  - Suplementasi zat besi (tablet tambah darah 60 mg Fe + 0,25 mg asam folat).\n"
        "  - Konseling gizi untuk meningkatkan asupan zat besi & vitamin.\n"
        "  - Evaluasi kadar Hb secara berkala.\n\n"
        "- **Anemia berat (Hb < 7 g/dL):**\n"
        "  - Perawatan di fasilitas kesehatan.\n"
        "  - Terapi zat besi dosis tinggi (oral/intravena sesuai indikasi).\n"
        "  - Transfusi darah bila diperlukan.\n\n"
        "- **Pendekatan umum:**\n"
        "  - Menangani penyebab lain: cacingan, malaria, perdarahan kronis.\n"
        "  - Pemantauan ketat selama kehamilan hingga persalinan."
    )

with st.expander("Quiz Singkat"):
    st.write("Coba jawab pertanyaan berikut untuk menguji pemahamanmu:")

    q1 = st.radio("1. Berapakah kadar Hb minimal yang dianggap normal pada ibu hamil?", 
                  ["9 g/dL", "10 g/dL", "11 g/dL", "12 g/dL"])
    if q1 == "11 g/dL":
        st.success("✅ Benar! Hb normal ibu hamil adalah ≥ 11 g/dL.")
    elif q1:
        st.error("❌ Belum tepat. Coba periksa kembali definisi anemia.")

    q2 = st.radio("2. Apa dampak anemia pada janin?", 
                  ["Prematur dan BBLR", "Kegemukan", "Mata minus", "Tidak ada pengaruh"])
    if q2 == "Prematur dan BBLR":
        st.success("✅ Benar! Anemia bisa menyebabkan prematur dan berat lahir rendah.")
    elif q2:
        st.error("❌ Kurang tepat. Coba cek kembali bagian Dampak.")
