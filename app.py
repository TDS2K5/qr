import streamlit as st
from pyzbar.pyzbar import decode
from PIL import Image

st.title("QR Code Decoder")

uploaded_file = st.file_uploader("Upload a QR ", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    result = decode(image)
    if result:
        
        st.success(f"Decoded text: {result[0].data.decode('utf-8')}")
    else:
        st.warning("No QR code found.")
