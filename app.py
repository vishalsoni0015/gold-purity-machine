import streamlit as st

st.set_page_config(page_title="Metal Purity Machine", layout="centered")

# Title
st.title("🔍 Gold & Silver Purity Testing Machine")
st.caption("AI-powered demo purity analyzer (chemical-free)")

# Inputs
material = st.selectbox(
    "Select Material",
    ["Gold", "Silver", "Fake Gold", "Copper"]
)

purity = st.slider(
    "Enter Purity (%)",
    0.0, 100.0, 90.0
)

# Logic
def machine_result(material, purity):
    if material == "Gold":
        status = "REAL GOLD ✅" if purity >= 91.6 else "FAKE ❌"
        confidence = min(purity, 99.9)
    elif material == "Silver":
        status = "REAL SILVER ✅" if purity >= 92.5 else "FAKE ❌"
        confidence = min(purity, 99.9)
    else:
        status = "FAKE / NOT PURE ❌"
        confidence = purity * 0.6

    return status, round(confidence, 2)

# Button
if st.button("🔎 SCAN MATERIAL"):
    status, confidence = machine_result(material, purity)

    st.subheader("📊 Scan Result")

    if "REAL" in status:
        st.success(status)
    else:
        st.error(status)

    st.write(f"**Confidence Level:** {confidence}%")
    st.progress(confidence / 100)

    st.info("⚠️ This is a software demo. Real machine will use sensor data.")
