import streamlit as st
import pandas as pd

# Tumhara sample data
data = {
    "Material": ["Gold", "Silver", "Fake Gold", "Copper"],
    "Purity": [99.9, 92.5, 50.0, 89.0]
}
df = pd.DataFrame(data)

# Tumhara function
def machine_result(material, purity):
    if material == "Gold":
        status = "REAL GOLD ✅"
    elif material == "Silver":
        status = "REAL SILVER ✅"
    else:
        status = "FAKE / NOT PURE ❌"
    return status

# Streamlit UI
st.title("Gold/Silver Purity Machine 🔥")
st.write("Ye machine bata rahi hai ki material real hai ya fake")

# Display results in table
for _, row in df.iterrows():
    status = machine_result(row["Material"], row["Purity"])
    st.write(f"**Material:** {row['Material']}")
    st.write(f"**Purity:** {row['Purity']}%")
    st.write(f"**Status:** {status}")
    st.write("---")
