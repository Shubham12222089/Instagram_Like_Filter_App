import streamlit as st
import cv2 as cv
import numpy as np

st.title("Apply Filters to Your Picture : ")

image = st.file_uploader("Upload Your Image :", type=['jpeg', 'jpg', 'png'])
r = st.text_input("Enter the color as R (0-255): ", "0")
g = st.text_input("Enter the color as G (0-255): ", "0")
b = st.text_input("Enter the color as B (0-255): ", "0")
a = st.text_input("Enter the alpha (0-1): ", "0.5")
be = st.text_input("Enter the beta (0-1): ", "0.5")

def tone(image, r, g, b, a, be):
    try:
        # Convert the inputs to the correct types
        r = int(r)
        g = int(g)
        b = int(b)
        a = float(a)
        be = float(be)

        # Ensure the RGB values are in the correct range
        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        color = [b, g, r]  # OpenCV uses BGR format

        if image is not None:
            # Convert the uploaded file to an OpenCV image
            file_bytes = np.asarray(bytearray(image.read()), dtype=np.uint8)
            img = cv.imdecode(file_bytes, 1)

            # Create a tone image of the same size as the input image
            tone_image = np.full_like(img, color)
            # or 
            # for i in range(rows):
            #     temp = []
            #     for j in range(cols):
            #         temp.append(blue)
            #     bg.append(temp)
            # bg = np.array(bg).astype(np.uint8)
            # Blend the original image with the tone
            final = cv.addWeighted(img, a, tone_image, be, 0)

            # Display the final image
            st.image(final, channels="BGR", caption="Tone Applied Image")
    except ValueError:
        st.write("Please enter valid numeric values.")

tone(image, r, g, b, a, be)
