import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Crypto Behaviour Dashboard", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.stApp {
    background-color: #f6f8fc;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("📊 Crypto Trader Behaviour Dashboard")
st.markdown("### Market Sentiment vs Trading Performance")

# load data
pnl = pd.read_csv("pnl_summary.csv")
win = pd.read_csv("win_summary.csv")
clusters = pd.read_csv("trader_clusters.csv")

# ---------- SIDEBAR ----------
st.sidebar.title("Project Overview")
st.sidebar.write("Analyze trader psychology using Fear & Greed Index")
st.sidebar.write("Model: Logistic Regression")
st.sidebar.write("Clustering: KMeans (3 trader types)")

# ---------- CHARTS ----------
col1, col2 = st.columns(2)

with col1:
    fig1 = px.bar(
        pnl,
        x="classification",
        y="closed_pnl",
        color="classification",
        title="Average PnL by Sentiment",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.bar(
        win,
        x="classification",
        y="win",
        color="classification",
        title="Win Rate by Sentiment",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    st.plotly_chart(fig2, use_container_width=True)

# ---------- CLUSTERS ----------
st.markdown("## 🧠 Trader Archetypes")
st.dataframe(clusters, use_container_width=True)

# ---------- INSIGHTS ----------
st.markdown("## 🔍 Key Insights")
st.info("""
• Highest profitability occurs during Extreme Greed  
• Fear markets cause aggressive and risky trading  
• Only a small group of traders remains consistently profitable
""")
