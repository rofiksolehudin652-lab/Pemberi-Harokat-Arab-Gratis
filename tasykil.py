import streamlit as st
import mishkal.tashkeel

# Judul Tab Browser
st.set_page_config(page_title="Al-Mu'rib: Harakat Otomatis", page_icon="🌙", layout="wide")

# Gaya Tampilan (CSS)
st.markdown("""
    <style>
    .main { background-color: #f9f9f9; }
    .stTextArea textarea { font-size: 22px !important; direction: rtl; }
    .stButton>button { background-color: #2e7d32; color: white; height: 3em; width: 100%; border-radius: 10px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌙 Al-Mu'rib: Aplikasi Harakat Bahasa Arab")
st.write("Berikan harakat pada teks Arab gundul secara otomatis.")
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        background-color: #007bff;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)
col1, col2 = st.columns(2)

with col1:
    text_input = st.text_area("Masukkan Teks Arab:", height=300)

with col2:
    if 'hasil_harakat' in st.session_state:
        st.text_area("Hasil Harakat:", value=st.session_state.hasil_harakat, height=300)

# Fungsi Mesin
@st.cache_resource
def siapkan_mesin():
    daftar = dir(mishkal.tashkeel)
    NamaKelas = getattr(mishkal.tashkeel, daftar[0])
    return NamaKelas()

# Tampilan Kolom Berdampingan
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Teks")
    tombol = st.button("✨ Beri Harakat Sekarang")
   text_input = st.text_area("Hasil Teks Arab:", height=300)
with col2:
    if tombol:
        if text_input.strip():
            with st.spinner("Sedang memproses..."):
                try:
                    mesin = siapkan_mesin()
                    hasil = mesin.tashkeel(text_input)
                    st.text_area("Hasil Harakat:", value=hasil, height=250)
                    st.balloons() # Efek balon saat sukses
                except Exception as e:
                    st.error(f"Maaf, ada kendala: {e}")
        else:
            st.warning("Silakan isi teks terlebih dahulu.")

# Informasi di bawah
st.divider()
st.caption("Dikembangkan oleh Rofik menggunakan Streamlit dan Mishkal AI.")
