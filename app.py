import streamlit as st
import pandas as pd
import datetime
import time

st.set_page_config(page_title="Mindful Work Pro+", layout="wide")

# ---------- UI STYLE ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

/* Card */
.card {
    background: rgba(255,255,255,0.15);
    backdrop-filter: blur(20px);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    margin-bottom: 20px;
    text-align: center;
    color: white;
}

/* BIG ICON BUTTONS */
.icon-btn {
    background: linear-gradient(135deg, #ff758c, #ff7eb3);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: white;
    margin: 10px;
    cursor: pointer;
    transition: 0.3s;
}

.icon-btn:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}

/* Bigger emoji */
.big-icon {
    font-size: 40px;
    display: block;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)
# ---------- LOAD DATA ----------
def load_data():
    try:
        df = pd.read_csv("stress_data.csv")
        df["Date"] = pd.to_datetime(df["Date"])
        return df
    except:
        return pd.DataFrame(columns=["Date","Stress"])

df = load_data()

# ---------- SESSION STATE ----------
if "page" not in st.session_state:
    st.session_state.page = "Home"

if "journal" not in st.session_state:
    st.session_state.journal = []

# ---------- NAVIGATION FUNCTION ----------
def navigate(page):
    st.session_state.page = page

# ---------- HOME PAGE ----------
if st.session_state.page == "Home":
    st.title("🌟 Mindful Work Pro+")

    st.markdown('<div class="card">Welcome 👋<br>Your personal stress companion</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📊 Dashboard", key="dash"):
            navigate("Dashboard")

        st.markdown("""
        <div class="icon-btn">
            <span class="big-icon">📊</span>
            Dashboard
        </div>
        """, unsafe_allow_html=True)

        if st.button("🤖 AI Coach", key="ai"):
            navigate("AI")

        st.markdown("""
        <div class="icon-btn">
            <span class="big-icon">🤖</span>
            AI Coach
        </div>
        """, unsafe_allow_html=True)

    with col2:
        if st.button("📈 Analytics", key="analytics"):
            navigate("Analytics")

        st.markdown("""
        <div class="icon-btn">
            <span class="big-icon">📈</span>
            Analytics
        </div>
        """, unsafe_allow_html=True)

        if st.button("🧘 Breathing", key="breath"):
            navigate("Breathing")

        st.markdown("""
        <div class="icon-btn">
            <span class="big-icon">🧘</span>
            Breathing
        </div>
        """, unsafe_allow_html=True)

    if st.button("📖 Journal"):
        navigate("Journal")

    st.markdown("""
    <div class="icon-btn">
        <span class="big-icon">📖</span>
        Journal
    </div>
    """, unsafe_allow_html=True)
# ---------- DASHBOARD ----------
elif st.session_state.page == "Dashboard":
    st.title("📊 Dashboard")

    if st.button("⬅ Back"):
        navigate("Home")

    stress = st.slider("Stress level", 0, 100, 50)

    if st.button("Save"):
        new = pd.DataFrame([[datetime.datetime.now(), stress]], columns=["Date","Stress"])
        new.to_csv("stress_data.csv", mode='a', header=False, index=False)
        st.success("Saved!")

    if not df.empty:
        st.line_chart(df.set_index("Date")["Stress"])

# ---------- ANALYTICS ----------
elif st.session_state.page == "Analytics":
    st.title("📈 Analytics")

    if st.button("⬅ Back"):
        navigate("Home")

    if not df.empty:
        weekly = df.resample('W-Mon', on='Date').mean()
        st.line_chart(weekly)

# ---------- AI ----------
elif st.session_state.page == "AI":
    st.title("🤖 AI Coach")

    if st.button("⬅ Back"):
        navigate("Home")

    stress = st.slider("Stress", 0, 100, 50)

    if st.button("Generate"):
        if stress > 70:
            st.error("Meditation + Calm Music")
        elif stress > 40:
            st.warning("Soft Music + Lights")
        else:
            st.success("Focus Mode")

# ---------- BREATHING ----------
elif st.session_state.page == "Breathing":
    st.title("🧘 Breathing")

    if st.button("⬅ Back"):
        navigate("Home")

    if st.button("Start"):
        placeholder = st.empty()
        for step in ["Inhale", "Hold", "Exhale"]:
            placeholder.subheader(step)
            time.sleep(2)

# ---------- JOURNAL ----------
elif st.session_state.page == "Journal":
    st.title("📖 Journal")

    if st.button("⬅ Back"):
        navigate("Home")

    entry = st.text_area("Write...")

    if st.button("Save"):
        st.session_state.journal.append(entry)

    for j in st.session_state.journal:
        st.write("•", j)