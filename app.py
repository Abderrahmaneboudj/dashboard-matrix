import streamlit as st
import os
import base64

# Create folders if they don't exist
folders = [
    "uploads/videos",
    "uploads/opencv",
    "uploads/yolo",
    "uploads/cropped",
    "uploads/ocr"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

st.set_page_config(layout="wide",
 page_icon="assets/matrix_logo.png",
 page_title=" Matrix Software Dashboard")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

logo_path = "assets/matrix_logo.png"
logo_base64 = get_base64_image(logo_path)

st.markdown(f"""
    <div style="text-align: center; padding-top: 10px;">
        <img src="data:image/png;base64,{logo_base64}" width="180">
        <h2 style="margin-top: 10px;">Container ISO Detection Dashboard</h2>
        <p style="color: gray; font-size: 16px;">
        Interactive dashboard to visualize each stage of a container ISO number detection pipeline
        </p>
    </div>
""", unsafe_allow_html=True)


# VIDEO SECTION

st.header("Video Display")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Video")
    input_video = st.file_uploader("Upload Raw Video", type=["mp4", "avi"])

    if input_video:
        path = f"uploads/videos/{input_video.name}"
        with open(path, "wb") as f:
            f.write(input_video.read())
        st.video(path)

with col2:
    st.subheader("Processed Video")
    output_video = st.file_uploader("Upload Processed Video", type=["mp4", "avi"])

    if output_video:
        path = f"uploads/videos/{output_video.name}"
        with open(path, "wb") as f:
            f.write(output_video.read())
        st.video(path)


# IMAGE PIPELINE SECTION

st.header("Pipeline Outputs")

col1, col2, col3 = st.columns(3)

# OpenCV Frame
with col1:
    st.subheader("OpenCV Frame")
    opencv_img = st.file_uploader("Upload OpenCV Image", type=["jpg", "png"])

    if opencv_img:
        path = f"uploads/opencv/{opencv_img.name}"
        with open(path, "wb") as f:
            f.write(opencv_img.read())
        st.image(path, caption="Frame from OpenCV")

# YOLO Output
with col2:
    st.subheader("YOLO Detection")
    yolo_img = st.file_uploader("Upload YOLO Image", type=["jpg", "png"])

    if yolo_img:
        path = f"uploads/yolo/{yolo_img.name}"
        with open(path, "wb") as f:
            f.write(yolo_img.read())
        st.image(path, caption="YOLO Bounding Box")

# Cropped Image
with col3:
    st.subheader("Cropped ISO Region")
    cropped_img = st.file_uploader("Upload Cropped Image", type=["jpg", "png"])

    if cropped_img:
        path = f"uploads/cropped/{cropped_img.name}"
        with open(path, "wb") as f:
            f.write(cropped_img.read())
        st.image(path, caption="Cropped Region")


# OCR SECTION

st.header("OCR Output")

col1, col2 = st.columns(2)

with col1:
    ocr_img = st.file_uploader("Upload OCR Image", type=["jpg", "png"])

    if ocr_img:
        path = f"uploads/ocr/{ocr_img.name}"
        with open(path, "wb") as f:
            f.write(ocr_img.read())
        st.image(path, caption="OCR Input")

with col2:
    st.subheader("Detected ISO Number")
    ocr_text = st.text_input("Enter OCR Output")

    if ocr_text:
        st.success(f"Detected: {ocr_text}")