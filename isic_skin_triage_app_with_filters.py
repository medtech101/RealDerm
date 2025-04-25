
import streamlit as st
import pandas as pd
import os

# Load synced metadata
df = pd.read_csv("ISIC_108_synced_metadata.csv")

st.set_page_config(page_title="ISIC Skin Triage Viewer", layout="centered")

st.title("🧠 ISIC Skin Triage Viewer")
st.write("Browse real skin condition images with AI-simulated triage information.")

# Sidebar filters
st.sidebar.header("🔍 Filter Images")
diagnosis_filter = st.sidebar.selectbox("Diagnosis", ["All"] + sorted(df["dx"].unique().tolist()))
severity_filter = st.sidebar.selectbox("Severity", ["All"] + sorted(df["severity"].unique().tolist()))
sex_filter = st.sidebar.selectbox("Sex", ["All"] + sorted(df["sex"].unique().tolist()))

# Apply filters
filtered_df = df.copy()
if diagnosis_filter != "All":
    filtered_df = filtered_df[filtered_df["dx"] == diagnosis_filter]
if severity_filter != "All":
    filtered_df = filtered_df[filtered_df["severity"] == severity_filter]
if sex_filter != "All":
    filtered_df = filtered_df[filtered_df["sex"] == sex_filter]

# Dropdown to select image
selected_id = st.selectbox("📷 Choose an image ID", filtered_df["image_id"])

if selected_id:
    record = filtered_df[filtered_df["image_id"] == selected_id].iloc[0]
    image_path = f"{selected_id}.jpg"

    if os.path.exists(image_path):
        st.image(image_path, caption=f"Image: {selected_id}", use_container_width=True)
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

    st.caption("📚 Simulated clinical context using the ISIC dataset (educational use only).")
