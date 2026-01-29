import streamlit as st
import pandas as pd
import plotly.express as px

# theme wrapper
st.markdown('<div class="theme-card">', unsafe_allow_html=True)

st.markdown("<h2 class='page-title'>📈 Market Analysis Dashboard</h2>", unsafe_allow_html=True)
st.markdown('<div class="section-underline"></div>', unsafe_allow_html=True)

st.write(
    "This dashboard demonstrates how I analyze market and performance data."
)

# ---- SAMPLE DATA ----
data = pd.DataFrame({
    "Brand": ["Vivo", "Samsung", "Oppo", "Infinix", "Xiaomi"],
    "Market_Share": [22, 25, 18, 20, 15]
})

# ---- CHART ----
fig = px.bar(
    data,
    x="Brand",
    y="Market_Share",
    title="Smartphone Market Share (%)",
    text="Market_Share"
)

fig.update_layout(yaxis_title="Market Share (%)")

st.plotly_chart(fig, use_container_width=True)

st.markdown(
    """
    **Insights:**
    - Market leaders can be identified quickly.
    - Supports competitor benchmarking.
    - Useful for sales & strategy planning.
    """
)

st.markdown('</div>', unsafe_allow_html=True)

try:
    from components.footer import render_footer
    render_footer()
except Exception:
    pass
