import streamlit as st
import qrcode
from io import BytesIO

st.title("QR Code Generator")

# user input
data = st.text_input("Enter text or URL for QR code:")

if st.button("Generate"):
    # make QR
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")

    # display in streamlit
    buf = BytesIO()
    img.save(buf, format="PNG")
    st.image(buf, caption="Your QR Code")

    # download option
    st.download_button(
        label="Download QR Code",
        data=buf.getvalue(),
        file_name="qr_code.png",
        mime="image/png"
    )
