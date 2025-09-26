import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🤖 Chatbot AI - DENIA")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if prompt := st.chat_input("Ketik pertanyaan Anda..."):
    st.session_state.chat_history.append(("user", prompt))

    try:
        # Panggil API OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Kamu adalah asisten kesehatan untuk ibu hamil."},
                *(
                    {"role": role, "content": text}
                    for role, text in st.session_state.chat_history
                ),
                {"role": "user", "content": prompt},
            ],
            max_tokens=100,      # batasi jawaban sekitar 100 token
            temperature=0.5      # jawaban tetap jelas tapi sedikit variatif
        )
        reply = response.choices[0].message.content
    except Exception as e:
        # Kalau error (misal saldo habis), tampilkan pesan aman
        reply = "⚠️ Chat AI saat ini sedang tidak tersedia. Silakan coba lagi nanti atau konsultasi dengan tenaga kesehatan."

    st.session_state.chat_history.append(("assistant", reply))

# Tampilkan riwayat chat
for role, text in st.session_state.chat_history:
    if role == "user":
        st.chat_message("user").markdown(text)
    else:
        st.chat_message("assistant").markdown(text)
