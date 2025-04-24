
import streamlit as st
import pandas as pd
import os

# Load metadata
df = pd.read_csv("HAM10000_sample_metadata.csv")

st.set_page_config(page_title="HAM10000 Skin Triage Viewer", layout="centered")

st.title("🧠 HAM10000 Skin Triage Viewer")
st.write("Browse real skin condition images with AI-simulated triage information.")

# Choose condition
selected_id = st.selectbox("📷 Choose an image ID", df['image_id'])

# Display info if selection is made
if selected_id:
    record = df[df['image_id'] == selected_id].iloc[0]
    image_path = f"images/{selected_id}.jpg"

    if os.path.exists(image_path):
        st.image(image_path, caption=f"Image: {selected_id}", use_column_width=True)
    else:
        st.warning("Image not found.")

    st.subheader("📋 Condition Summary")
    st.markdown(f"**Diagnosis:** {record['dx'].capitalize()}")
    st.markdown(f"**Severity:** `{record['severity']}`")
    st.markdown(f"**Suggested Action:** {record['suggested_action']}")
    st.markdown(f"""
**Age:** {record['age']}  
**Sex:** {record['sex']}  
**Location:** {record['localization']}
""")

    st.caption("📚 Simulated clinical context using the HAM10000 dataset (educational use only).")
