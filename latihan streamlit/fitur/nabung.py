import streamlit as st

st.title("Halaman Menabung")

# halaman menabung
with st.form("menabung"):
    nama = st.text_input("Nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0)
    submit_button = st.form_submit_button(label="Simpan")
    if submit_button:
        st.session_state['total_semua'].append({
            "Tipe": "menabung",
            "nama" : nama,
            "jumlah" : jumlah
        })
        st.success("Anda Berhasil Menabung")

    else:
        st.error("Anda Gagal Menabung")