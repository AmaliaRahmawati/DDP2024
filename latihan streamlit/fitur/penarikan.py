import streamlit as st

st.title("Halaman Penarikan")
st.image("bank.png", caption="ini gambar bank")

with st.form("penarikan"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    submit_button = st.form_submit_button(label="Simpan")
    if submit_button:
        st.session_state['total_semua'].append({
            "Tipe": "Penarikan",
            "nama" : nama,
            "jumlah" : jumlah
        })
        st.success("Anda Berhasil Penarikan")

    else:
        st.error("Anda Gagal Penarikan")