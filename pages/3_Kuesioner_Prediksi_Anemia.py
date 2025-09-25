import streamlit as st

st.title("📝 Kuesioner Prediksi Anemia")

st.write("Jawablah pertanyaan berikut dengan **Ya** atau **Tidak**:")

questions = [
    "Apakah anda merasa cepat lelah?",
    "Apakah anda merasa letih / lesu, seperti kelelahan sehabis bekerja berat?",
    "Apakah anda sering pusing?",
    "Apakah anda lebih sering bingung akhir akhir ini daripada sebelumnya?",
    "Apakah anda lebih pucat dari biasanya? (dapat terlihat dari warna bibir)",
    "Apakah anda sering mengalami sesak nafas?",
    "Apakah anda mengalami nyeri dada?",
    "Apakah tangan dan kaki terasa dingin?",
    "Apakah anda sulit berkonsentrasi?"
]

yes_count = 0

# Render pertanyaan dengan radio button
for q in questions:
    answer = st.radio(q, ["Tidak", "Ya"], index=0, key=q)
    if answer == "Ya":
        yes_count += 1

# Hitung hasil
if st.button("Hitung Hasil"):
    total_questions = len(questions)
    percent_yes = (yes_count / total_questions) * 100
    st.success(f"✅ Kemungkinan anemia berdasarkan kuesioner: **{percent_yes:.0f}%**")

    # Interpretasi sederhana
    if percent_yes >= 60:
        st.error("Hasil menunjukkan kemungkinan anemia cukup tinggi. Sebaiknya lakukan pemeriksaan Hb di fasilitas kesehatan.")
    elif percent_yes >= 30:
        st.warning("Ada beberapa gejala anemia. Perlu diwaspadai dan pertimbangkan pemeriksaan lebih lanjut.")
    else:
        st.info("Kemungkinan anemia rendah berdasarkan kuesioner ini. Tetap jaga pola makan dan kesehatan.")
