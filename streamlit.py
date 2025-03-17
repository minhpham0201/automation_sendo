import streamlit as st
from datetime import date
from modules import collate, utilities_sos, utilities_tms
from processing import processing_sos, processing_tms

# Function mapping
FUNCTIONS = {
    "Download Trip": lambda: st.write("Running Download Trip..."),
    "Download Shipment": lambda: st.write("Running Download Shipment..."),
    "Collate Trip": lambda: collate.trip_collate(),
    "Collate Shipment": lambda: collate.shipment_collate(),
    "Process TMS": lambda: processing_tms.process(),
    "Download Sorting": lambda: utilities_tms.download_sorting(),
    "Collate Sorting": lambda: utilities_tms.collate_sorting(),
    "Download OB": lambda: utilities_sos.download_ob(),
    "Collate OB": lambda: utilities_sos.collate_ob(),
    "Download Manifest": lambda: utilities_sos.download_manifest(),
    "Collate Manifest": lambda: utilities_sos.collate_manifest(),
}

# Streamlit App
st.title("Automation GUI")

# Calendar Input
selected_date = st.date_input(
    "Choose a Date:",
    min_value=date(2022, 1, 1),  # Adjust as needed
    max_value=date.today(),
    value=date.today(),
)

# Function Selector
selected_function = st.selectbox("Choose a Function:", list(FUNCTIONS.keys()))

# Run Button
if st.button("Run"):
    st.write(f"Date Selected: {selected_date}")
    st.write(f"Function Selected: {selected_function}")
    try:
        # Execute the selected function
        FUNCTIONS[selected_function]()
        st.success("Function executed successfully!")
    except Exception as e:
        st.error(f"Error occurred: {str(e)}")
