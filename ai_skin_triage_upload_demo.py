
import streamlit as st
import pandas as pd
from PIL import Image
import os
import random

# Load metadata
df = pd.read_csv("ISIC_108_synced_metadata.csv")

st.set_page_config(page_title="AI Derm Triage Demo", layout="centered")
st.title("🤖 AI-Enhanced Skin Triage Viewer")
st.write("Upload a skin lesion image to simulate AI-based diagnosis and triage support.")

# Upload image
uploaded_file = st.file_uploader("📷 Upload a skin image", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Simulate AI prediction
    st.subheader("🧠 Simulated AI Prediction")
    predicted_dx = random.choice(["melanoma", "nv", "bcc", "akiec"])
    predicted_severity = random.choice(["High - Urgent", "Medium", "Low - Benign", "Medium - Precancerous"])
    suggested_action = {
        "High - Urgent": "Urgent derm referral for biopsy",
        "Medium": "Derm referral for possible excision",
        "Medium - Precancerous": "Biopsy or monitor with dermatoscope",
        "Low - Benign": "Routine monitoring unless changes noted"
    }[predicted_severity]

    st.markdown(f"**Predicted Diagnosis:** `{predicted_dx}`")
    st.markdown(f"**Predicted Severity:** `{predicted_severity}`")
    st.markdown(f"**Suggested Action:** {suggested_action}")
    st.caption("📘 This is a simulated AI result. For demo purposes only.")
