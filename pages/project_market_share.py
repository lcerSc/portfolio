import streamlit as st
import pandas as pd
import plotly.express as px
import time

st.title("Market Share Explorer — Demo")

st.markdown(
    """
    Interactive demo: select brands and replay market-share evolution over months.
    """
)

# Sample timeseries data
months = pd.date_range("2023-01-01", periods=12, freq="M")
sample = pd.DataFrame({
    "date": list(months) * 5,
    "Brand": ["Vivo"] * 12 + ["Samsung"] * 12 + ["Oppo"] * 12 + ["Infinix"] * 12 + ["Xiaomi"] * 12,
    "Market_Share": [22,21,23,22,24,23,22,21,22,23,24,22, 25,24,26,25,24,25,26,25,24,25,26,25, 18,17,19,18,17,18,17,18,19,18,17,18, 20,19,20,21,20,19,21,20,19,20,21,20, 15,16,15,14,15,14,15,16,15,14,15,16]
})

brands = sample['Brand'].unique().tolist()
sel = st.multiselect("Select brands", brands, default=brands)

smooth = st.checkbox("Smooth lines (7-day rolling)")

chart_placeholder = st.empty()

def plot_until(n):
    df = sample[sample['Brand'].isin(sel) & (sample['date'] <= sample['date'].unique()[n-1])]
    if smooth:
        # simple rolling per brand
        df = df.sort_values('date').groupby('Brand').apply(lambda g: g.assign(Market_Share=g['Market_Share'].rolling(3, min_periods=1).mean())).reset_index(drop=True)
    fig = px.line(df, x='date', y='Market_Share', color='Brand', markers=True)
    fig.update_layout(yaxis_title='Market Share (%)')
    chart_placeholder.plotly_chart(fig, use_container_width=True)

if st.button("Replay demo"):
    total = len(sample['date'].unique())
    for i in range(1, total + 1):
        plot_until(i)
        time.sleep(0.18)

# Show full chart by default
if not st.session_state.get('replayed', False):
    fig_full = px.line(sample[sample['Brand'].isin(sel)], x='date', y='Market_Share', color='Brand', markers=True)
    fig_full.update_layout(yaxis_title='Market Share (%)')
    chart_placeholder.plotly_chart(fig_full, use_container_width=True)

st.markdown("---")
st.subheader("Notes")
st.write("This demo uses mock data; replace with real CSV ingestion for production dashboards.")

