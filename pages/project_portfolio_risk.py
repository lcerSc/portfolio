
import streamlit as st
import pandas as pd
import plotly.express as px
import time
import numpy as np

st.title("Portfolio Risk Heatmap — Demo")

st.markdown(
    """
    Interactive risk demo: simulate changing risk scores across regions and replay the heatmap evolution.
    """
)

data = pd.DataFrame([
    {"region": "North", "risk_score": 78},
    {"region": "South", "risk_score": 54},
    {"region": "East", "risk_score": 89},
    {"region": "West", "risk_score": 45}
])

vol = st.slider("Simulation volatility", 0.0, 30.0, 8.0)
threshold = st.slider("Alert threshold", 0, 100, 75)

ph = st.empty()

def plot_scores(df):
    fig = px.bar(df, x='region', y='risk_score', color='region')
    fig.update_layout(yaxis_title='Risk Score')
    ph.plotly_chart(fig, use_container_width=True)

if st.button("Replay demo"):
    # build a frames dataframe for animation (non-blocking)
    frames = []
    current = data.copy()
    for step in range(12):
        # random walk
        current = current.copy()
        current['risk_score'] = (current['risk_score'] + np.random.normal(0, vol, size=len(current))).clip(0, 100)
        current['step'] = step
        frames.append(current)

    df_frames = pd.concat(frames, ignore_index=True)
    fig = px.bar(df_frames, x='region', y='risk_score', color='region', animation_frame='step', range_y=[0,100], labels={'risk_score':'Risk Score'})
    fig.update_layout(coloraxis_showscale=False)
    ph.plotly_chart(fig, use_container_width=True)

    # show a simple alerts summary for the final simulated frame
    final = df_frames[df_frames['step'] == df_frames['step'].max()]
    high = final[final['risk_score'] > threshold]
    if not high.empty:
        st.warning(f"High risk detected (final frame): {', '.join(high['region'].tolist())}")
else:
    plot_scores(data)

st.markdown("---")
st.write("Use the replay to demonstrate how alerts can surface changing exposures.")
