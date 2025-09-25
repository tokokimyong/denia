import streamlit as st
import numpy as np
from PIL import Image, ImageOps
from streamlit_cropper import st_cropper

st.set_page_config(page_title="Deteksi Dini Anemia", layout="wide")
st.title("📸 Deteksi Dini Anemia - Prediksi Hemoglobin")

uploaded_file = st.file_uploader("Upload foto palpebra (jpg/png)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # 1) Buka & auto-rotate EXIF (fix iPhone rotation)
    image = Image.open(uploaded_file)
    image = ImageOps.exif_transpose(image)
    image = image.convert("RGB")  # pastikan RGB

    # 2) Resize untuk cropper agar pas di layar HP (opsional: user bisa atur)
    max_width = st.sidebar.slider("Resize max width untuk cropper (px)", 240, 800, 420)
    if image.width > max_width:
        ratio = max_width / float(image.width)
        new_h = int(image.height * ratio)
        image_for_crop = image.resize((max_width, new_h))
    else:
        image_for_crop = image

   

    st.write("### Pilih ROI (area palpebra konjungtiva)")
    # Pastikan return_type='image' agar kita langsung dapat PIL.Image
    cropped_img = st_cropper(
        image_for_crop,
        realtime_update=True,
        box_color="red",
        aspect_ratio=None,
        return_type="image",  # penting: pakai 'image' agar hasilnya PIL.Image
        key="cropper"
    )

    # 3) Validasi hasil crop sebelum proses numpy
    if cropped_img is None:
        st.warning("Silakan tarik kotak crop untuk memilih ROI terlebih dahulu.")
    else:
        # Pastikan cropped_img adalah PIL.Image dan ukurannya > 0
        if hasattr(cropped_img, "size"):
            w, h = cropped_img.size
            if w == 0 or h == 0:
                st.error("ROI yang dipilih kosong (width/height = 0). Silakan pilih area yang valid.")
            else:
                # Convert to numpy array dan pastikan shape benar
                arr = np.array(cropped_img).astype(np.float32)  # H x W x 3
                if arr.ndim != 3 or arr.shape[2] < 3:
                    st.error("ROI bukan format RGB. Pastikan gambar berwarna (RGB).")
                else:
                    # Hitung mean RGB dengan aman
                    try:
                        mean_rgb = arr.mean(axis=(0, 1))
                    except Exception as e:
                        st.error(f"Gagal menghitung rata-rata RGB: {e}")
                        st.exception(e)
                    else:
                        mean_rgb_int = mean_rgb.astype(int)
                        st.write(f"Rata-rata RGB ROI (daerah terpilih): {mean_rgb_int.tolist()}")

                        # Prediksi Hb (persamaan Anda)
                        R = float(mean_rgb[0])
                        pred_hb = (R - 63.695) / 12.258
                        st.success(f"✅ Prediksi Kadar Hemoglobin: **{pred_hb:.2f} g/dL**")

                        # Kategori sederhana
                        if pred_hb > 10.9:
                            keterangan = "Normal"
                        elif pred_hb >= 8.1:
                            keterangan = "Anemia Ringan"
                        elif pred_hb >= 6.5:
                            keterangan = "Anemia Sedang"
                        else:
                            keterangan = "Anemia Berat"
                        st.info(f"Keterangan: **{keterangan}**")
        else:
            st.error("Hasil crop bukan gambar. Pastikan `return_type='image'` pada st_cropper.")
