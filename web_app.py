import streamlit as st
import cv2
import numpy as np

def linear_transform(image, alpha=1.0, beta=0):
    new_img = alpha * image + beta
    new_img = np.clip(new_img, 0, 255)
    return new_img.astype(np.uint8)

st.title("Image Contrast Enhancement")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    alpha = st.slider("Contrast (alpha)", 0.5, 3.0, 1.5)
    beta = st.slider("Brightness (beta)", 0, 100, 20)

    enhanced = linear_transform(gray, alpha, beta)

    st.image(gray, caption="Original", channels="GRAY")
    st.image(enhanced, caption="Enhanced", channels="GRAY")