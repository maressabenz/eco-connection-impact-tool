
import streamlit as st
from utils.calculations import calculate_co2_savings, calculate_water_savings

st.set_page_config(page_title="Eco Connection Dashboard", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Circular Economy", "Product Swaps", "Low-Carbon Lifestyle", "Knowledge Hub"])

if page == "Home":
    st.title("Track your impact. Consume less. Create more.")
    st.write("See how small changes add up to big climate wins.")
    col1, col2, col3 = st.columns(3)
    col1.metric("CO2 saved", "125 kg")
    col2.metric("Water saved", "1800 l")
    col3.metric("Items diverted from landfill", "5")

elif page == "Circular Economy":
    st.header("Log your circular actions")
    action = st.selectbox("What did you do?", ["Reused item", "Repaired item", "Upcycled", "Shared/Rented"])
    co2_saved = calculate_co2_savings(action)
    st.success(f"You saved approximately {co2_saved} kg CO2 (Source: IPCC AR6 WGIII, 2022)")
    st.text_area("Add private notes (optional)")
    st.text_input("Feedback for us?")
    st.select_slider("How do you feel today?", options=["😐", "🙂", "😃", "🤩"])

elif page == "Product Swaps":
    st.header("Eco-friendly product swap calculator")
    st.write("Example: Switch from disposable to reusable water bottle.")

elif page == "Low-Carbon Lifestyle":
    st.header("Track your low-carbon choices")

elif page == "Knowledge Hub":
    st.header("Learn and take action")
    st.markdown("- [IPCC AR6 Summary for Policymakers](https://www.ipcc.ch/report/ar6/wg3/)")
