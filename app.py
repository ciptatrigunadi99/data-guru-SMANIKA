import streamlit as st

# Pengaturan Judul Halaman
st.set_page_config(page_title="BioBot: Belajar Biologi", page_icon="🌿")

st.title("🌿 BioBot: Chatbot Pembelajaran Biologi")
st.write("Halo! Saya adalah asisten virtualmu untuk belajar Biologi. Tanyakan sesuatu tentang Sel, Fotosintesis, atau DNA!")

# Inisialisasi riwayat chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Logika Respon Chatbot (Sederhana)
def get_bot_response(user_input):
    user_input = user_input.lower()
    
    if "sel" in user_input:
        return "Sel adalah unit terkecil dari makhluk hidup. Ada sel prokariotik (tanpa inti) dan eukariotik (dengan inti)."
    elif "fotosintesis" in user_input:
        return "Fotosintesis adalah proses tumbuhan hijau mengubah energi cahaya menjadi energi kimia (glukosa) menggunakan air dan CO2."
    elif "dna" in user_input:
        return "DNA (Asam Deoksiribonukleat) adalah materi genetik yang membawa instruksi biologis untuk pertumbuhan dan fungsi organisme."
    elif "halo" in user_input or "hi" in user_input:
        return "Halo! Ada materi biologi yang ingin kamu diskusikan hari ini?"
    else:
        return "Maaf, saya masih belajar. Coba tanyakan tentang 'Sel', 'Fotosintesis', atau 'DNA'."

# Input pengguna
if prompt := st.chat_input("Ketik pertanyaan biologi di sini..."):
    # Tambahkan pesan pengguna ke riwayat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Berikan respon bot
    response = get_bot_response(prompt)
    
    # Tambahkan respon bot ke riwayat
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})