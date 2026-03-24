import streamlit as st
import cv2
import numpy as np

def linear_transform(image, alpha=1.0, beta=0):
    new_img = alpha * image.astype(np.float32) + beta
    new_img = np.clip(new_img, 0, 255)
    return new_img.astype(np.uint8)

st.title("Image Contrast Enhancement (Color)")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    alpha = st.slider("Contrast (alpha)", 0.5, 3.0, 1.5)
    beta = st.slider("Brightness (beta)", 0, 100, 20)

    enhanced = linear_transform(image, alpha, beta)

    st.image(image, caption="Original Image")
    st.image(enhanced, caption="Enhanced Image")
