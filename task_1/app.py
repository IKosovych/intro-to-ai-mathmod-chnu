import io
from PIL import Image

import streamlit as st

st.write("# Lab 1 - Image Uploader")

uploaded_file = st.file_uploader(
    "Pick a file", type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_file is not None:
    try:
        image_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption='Uploaded Image', use_column_width=True)
    except Exception as e:
        st.error(f"Could not open image: {e}")
else:
    st.info("Please upload an image file.")
