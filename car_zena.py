import streamlit as st
import pandas as pd

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="DickSound Auto Workshop",
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
menu = st.sidebar.radio("📍 MENU", ["🏠 Home", "🔧 Services", "📲 Book Service"])

# =========================
# HOME PAGE
# =========================
if menu == "🏠 Home":

    st.markdown(
        """
        <h1 style='text-align:center; color:#1F618D;'>
        🚗 DickSound Auto Workshop
        </h1>
        <p style='text-align:center; font-size:18px;'>
        Book car services like painting, android installation, rim fixing & more
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # METRIC CARDS
    col1, col2, col3 = st.columns(3)

    col1.metric("🚗 Total Services", len(data))
    col2.metric("✅ Completed", len(data[data["Status"] == "Completed"]))
    col3.metric("⏳ Pending", len(data[data["Status"] == "Pending"]))

    st.markdown("---")

    # CHART
    st.subheader("📊 Price Overview")
    st.bar_chart(data.set_index("Service")["Price (Tsh)"])

# =========================
# SERVICES PAGE
# =========================
elif menu == "🔧 Services":

    st.markdown(
        "<h2 style='color:#1F618D;'>🔧 Available Services</h2>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.dataframe(data, use_container_width=True)

# =========================
# BOOKING PAGE
# =========================
elif menu == "📲 Book Service":

    st.markdown(
        "<h2 style='color:#25D366;'>📲 Book a Service</h2>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    phone_number = "255718632621"  # 👉 change to your real number

    service = st.selectbox("Choose a service", data["Service"])

    message = f"Hello 👋, I want to book {service} from Carzena Auto Workshop."

    whatsapp_url = f"https://wa.me/{phone_number}?text={message}"

    st.markdown(
        f"""
        <a href="{whatsapp_url}" target="_blank">
            <div style="
            background:#25D366;
            padding:18px;
            border-radius:15px;
            text-align:center;
            color:white;
            font-size:18px;
            font-weight:bold;
            cursor:pointer;">
            📲 BOOK SERVICE ON WHATSAPP
            </div>
        </a>
        """,
        unsafe_allow_html=True
    )
