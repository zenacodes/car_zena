import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="DickSound Workshop Dashboard",
    page_icon="🚗",
    layout="wide"
)

# =========================
# DATA
# =========================
data = pd.DataFrame({
    "Service": [
        "Car Painting",
        "Android Installation",
        "Rim Installation",
        "Seat Cover Change",
        "Car Upgrading"
    ],
    "Price (Tsh)": [500000, 250000, 150000, 120000, 800000],
    "Status": ["Completed", "Completed", "Pending", "Completed", "Pending"]
})

# =========================
# SIDEBAR MENU
# =========================
menu = st.sidebar.selectbox(
    "📍 MENU",
    ["🏠 Home", "🔧 Services", "📲 Book Service"]
)

# =========================
# HOME PAGE
# =========================
if menu == "🏠 Home":

    st.markdown(
        "<h1 style='text-align:center; color:#2E86C1;'>🚗 DickSound Workshop Dashboard</h1>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Services", len(data))
    col2.metric("Completed", len(data[data["Status"] == "Completed"]))
    col3.metric("Pending", len(data[data["Status"] == "Pending"]))

    st.markdown("---")

    st.subheader("📊 Price Overview")
    st.bar_chart(data.set_index("Service")["Price (Tsh)"])

# =========================
# SERVICES PAGE
# =========================
elif menu == "🔧 Services":

    st.markdown(
        "<h2 style='color:#2E86C1;'>🔧 Our Services </h2>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.dataframe(data, use_container_width=True)

# =========================
# BOOKING PAGE
# =========================
elif menu == "📲 Book Service":

    st.markdown(
        "<h2 style='color:#25D366;'>📲 Book a Service via WhatsApp</h2>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    phone_number = "255718632621" 

    service = st.selectbox("Choose a service", data["Service"])

    message = f"Hello, I want to book: {service} at your workshop."

    whatsapp_url = f"https://wa.me/{phone_number}?text={message}"

    st.markdown(
        f"""
        <a href="{whatsapp_url}" target="_blank">
            <button style="
            background-color:#25D366;
            color:white;
            padding:15px;
            border:none;
            border-radius:12px;
            width:100%;
            font-size:18px;
            font-weight:bold;
            cursor:pointer;">
            📲 Book Service on WhatsApp
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )
