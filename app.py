import streamlit as st

# Data Guru Lembaga Sekolah
DATA_GURU = [
    {"nama": "Budi Santoso, S.Pd.", "mapel": "Biologi", "jabatan": "Guru Wali Kelas X"},
    {"nama": "Siti Rahma, M.Pd.", "mapel": "Matematika", "jabatan": "Kepala Laboratorium"},
    {"nama": "Ahmad Fauzi, S.T.", "mapel": "Informatika", "jabatan": "Pembina Ekstrakurikuler"},
    {"nama": "Dewi Lestari, S.S.", "mapel": "Bahasa Inggris", "jabatan": "Guru Wali Kelas XI"}
]

# Pengaturan Halaman
st.set_page_config(page_title="Informasi Guru Sekolah", page_icon="🏫")
st.title("🏫 Chatbot Informasi Guru Sekolah")
st.write("Cari informasi guru berdasarkan **nama** atau **mata pelajaran** (contoh: *Biologi*, *Budi*, *Daftar Guru*).")

# Inisialisasi riwayat percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan riwayat chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Fungsi pencarian guru
def cari_guru(query):
    query = query.lower()
    
    if "semua" in query or "daftar" in query or "list" in query:
        respon = "**Daftar Seluruh Guru:**\n"
        for g in DATA_GURU:
            respon += f"- **{g['nama']}** ({g['mapel']}) - *{g['jabatan']}*\n"
        return respon

    hasil = []
    for g in DATA_GURU:
        if query in g["nama"].lower() or query in g["mapel"].lower():
            hasil.append(f"• **{g['nama']}**\n  - Mata Pelajaran: {g['mapel']}\n  - Peran/Jabatan: {g['jabatan']}")
    
    if hasil:
        return "Berikut informasi guru yang ditemukan:\n\n" + "\n\n".join(hasil)
    else:
        return "Maaf, data guru atau mata pelajaran tersebut tidak ditemukan. Ketik **'Daftar'** untuk melihat semua data."

# Input dari pengguna
if prompt := st.chat_input("Tanyakan nama guru atau mapel..."):
    # Tampilkan pesan pengguna
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Dapatkan respon bot
    respon_bot = cari_guru(prompt)
    
    # Tampilkan respon bot
    with st.chat_message("assistant"):
        st.markdown(respon_bot)
    st.session_state.messages.append({"role": "assistant", "content": respon_bot})
