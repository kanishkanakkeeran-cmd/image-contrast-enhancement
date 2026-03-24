import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt

def linear_transform(image, alpha, beta):
    new_img = alpha * image + beta
    new_img = np.clip(new_img, 0, 255)
    return new_img.astype(np.uint8)

st.title("Image Contrast Enhancement")

uploaded_file = st.file_uploader("Upload Image", type=["jpg","png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    alpha = st.slider("Contrast", 0.5, 3.0, 1.5)
    beta = st.slider("Brightness", 0, 100, 20)

    enhanced = linear_transform(gray, alpha, beta)

    st.image(gray, caption="Original", channels="GRAY")
    st.image(enhanced, caption="Enhanced", channels="GRAY")

    # Histogram Graph
    fig, ax = plt.subplots()
    ax.hist(gray.ravel(), bins=256, alpha=0.5, label='Original')
    ax.hist(enhanced.ravel(), bins=256, alpha=0.5, label='Enhanced')
    ax.legend()
    st.pyplot(fig)
