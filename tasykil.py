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

st.title("🌙 Al-Mu'rib: Aplikasi Harakat Arab")
st.write("Berikan harakat pada teks Arab gundul secara instan.")

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
    text_input = st.text_area("Tempelkan teks Arab di sini:", placeholder="...مرحبا كيف حالك", height=300)
    tombol = st.button("✨ Beri Harakat Sekarang")

with col2:
    st.subheader("Hasil")
    if tombol:
        if text_input.strip():
            with st.spinner("Sedang memproses..."):
                try:
                    mesin = siapkan_mesin()
                    hasil = mesin.tashkeel(text_input)
                    st.text_area("Hasil Harakat:", value=hasil, height=300)
                    st.balloons() # Efek balon saat sukses
                except Exception as e:
                    st.error(f"Maaf, ada kendala: {e}")
        else:
            st.warning("Silakan isi teks terlebih dahulu.")

# Informasi di bawah
st.divider()
st.caption("Dikembangkan dengan Rofik menggunakan Streamlit dan Mishkal AI.")
