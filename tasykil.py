import streamlit as st
import mishkal.tashkeel

st.set_page_config(page_title="Pemberi Harakat Arab", page_icon="🌙")
st.title("Aplikasi Harakat Arab Otomatis")

# Fungsi untuk menyiapkan mesin harakat
@st.cache_resource
def siapkan_mesin():
    # Mengambil kelas pertama yang ditemukan di library kamu
    daftar = dir(mishkal.tashkeel)
    NamaKelas = getattr(mishkal.tashkeel, daftar[0])
    # Menyalakan mesin (inisialisasi)
    return NamaKelas()

text_input = st.text_area("Masukkan teks Arab gundul:", height=200)

if st.button("Munculkan Harakat ✨"):
    if text_input.strip():
        try:
            mesin = siapkan_mesin()
            # Mencoba perintah harakat yang paling umum
            hasil = mesin.tashkeel(text_input)
            st.success("Selesai!")
            st.text_area("Hasil:", value=hasil, height=200)
        except Exception as e:
            st.error(f"Gagal memproses. Detail: {e}")
    else:
        st.warning("Silakan isi teksnya dulu.")