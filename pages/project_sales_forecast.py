
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("Sales Forecast Model — Demo")

st.markdown(
    """
    Interactive sales forecast demo: adjust growth and horizon, then run to see a simple simulated forecast.
    """
)

# sample historical data
dates = pd.date_range("2023-01-01", periods=12, freq='M')
hist = pd.Series([1200, 1350, 1280, 1400, 1500, 1550, 1490, 1600, 1620, 1700, 1680, 1750], index=dates)
df_hist = pd.DataFrame({"date": dates, "sales": hist.values})

col1, col2 = st.columns(2)
with col1:
    growth = st.slider("Monthly growth assumption (%)", -5.0, 10.0, 2.0, step=0.5)
with col2:
    months_ahead = st.slider("Forecast horizon (months)", 1, 12, 6)

placeholder = st.empty()

def simulate_forecast(base_df, growth_pct, horizon):
    # base_df must have a 'date' column and a 'sales' column
    last = base_df['sales'].iloc[-1]
    last_date = pd.to_datetime(base_df['date'].iloc[-1])
    dates = pd.date_range(last_date + pd.offsets.MonthEnd(1), periods=horizon, freq='M')
    preds = []
    val = last
    for _ in range(horizon):
        val = val * (1 + growth_pct / 100.0) + np.random.normal(0, val * 0.02)
        preds.append(val)
    df_future = pd.DataFrame({"date": dates, "sales": np.round(preds, 0)})
    return df_future

if st.button("Run forecast"):
    df_future = simulate_forecast(df_hist, growth, months_ahead)
    df_plot = pd.concat([df_hist, df_future], ignore_index=True)
    fig = px.line(df_plot, x='date', y='sales', markers=True)
    fig.add_vline(x=df_hist['date'].iloc[-1], line_dash="dash", annotation_text="Today", annotation_position="top right")
    placeholder.plotly_chart(fig, use_container_width=True)
    csv = df_future.to_csv(index=False)
    st.download_button("Download forecast CSV", data=csv, file_name="forecast.csv")
else:
    fig = px.line(df_hist, x='date', y='sales', markers=True)
    placeholder.plotly_chart(fig, use_container_width=True)

