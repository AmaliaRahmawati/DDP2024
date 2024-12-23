import streamlit as st
# Side bar directory
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
Nabung = st.Page("./fitur/nabung.py", title="Nabung")
penarikan = st.Page("./fitur/penarikan.py", title="Penarikan")

pg = st.navigation(
    {
        "Menu utama": [dashboard],
        "transaksi": [Nabung, penarikan],
    }
)


if 'total_semua' not in st.session_state:
    st.session_state['total_semua'] = []


# Menjalankan navigasi
pg.run()


