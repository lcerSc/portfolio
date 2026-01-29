import streamlit as st
import pandas as pd
import plotly.express as px

# theme wrapper
st.markdown('<div class="theme-card">', unsafe_allow_html=True)

st.markdown("<h2 class='page-title'>📂 Projects</h2>", unsafe_allow_html=True)
st.markdown('<div class="section-underline"></div>', unsafe_allow_html=True)

# sample project cards
st.markdown('<div class="project-grid">', unsafe_allow_html=True)
projects = [
    {"title":"Market Share Explorer","desc":"Interactive dashboards for competitive analysis and share tracking.", "icon":"📊", "tags":["Dashboards","Plotly"], "page":"pages/project_market_share.py"},
    {"title":"Sales Forecast Model","desc":"Time-series forecasting and scenario planning for revenue.", "icon":"📈", "tags":["Forecasting","ARIMA"], "page":"pages/project_sales_forecast.py"},
    {"title":"Portfolio Risk Heatmap","desc":"Risk scoring and visualization for portfolio exposures.", "icon":"🗺️", "tags":["Risk","Visualization"], "page":"pages/project_portfolio_risk.py"}
]
for p in projects:
    tags_html = ''.join([f"<div class='project-tag'>{t}</div>" for t in p.get('tags', [])])
    st.markdown(f"<div class='project-card fade-in'><div><h4><span class='project-icon'>{p['icon']}</span>{p['title']}</h4><p>{p['desc']}</p></div><div class='meta'><div class='project-tags'>{tags_html}</div><a class='project-cta' href='/?page={p['page']}'>View</a></div></div>", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Feature Projects (detailed cards) ---
st.markdown("<div style='margin-top:18px'></div>", unsafe_allow_html=True)
st.markdown("<h3 style='margin-bottom:6px;'>Featured Projects</h3>", unsafe_allow_html=True)
st.markdown('<div class="section-underline" style="width:120px"></div>', unsafe_allow_html=True)

featured = [
    {
        "title": "Market Share Explorer",
        "problem": "Product teams lacked a quick way to compare competitors across regions and time.",
        "data": "Sales & shipment logs (CSV), public market reports",
        "tools": "Python, Pandas, Plotly, Streamlit",
        "what": "Built an interactive dashboard with drill-down filters by region, time, and brand. Automated data ingestion and smoothing of noisy weekly reports.",
        "impact": "Reduced analysis time from days to minutes; informed pricing and distribution decisions that improved market share by 3% in target regions.",
        "impact_pct": 3,
        "tags": ["Dashboards","Market"],
        "repo": "#",
        "sample_data": [
            {"Brand":"Vivo","Market_Share":22},{"Brand":"Samsung","Market_Share":25},{"Brand":"Oppo","Market_Share":18}
        ]
    },
    {
        "title": "Sales Forecast Model",
        "problem": "Leadership needed robust short-term revenue forecasts for planning promotions.",
        "data": "Historical sales (ERP), promotions calendar, macro indicators",
        "tools": "Python, Prophet/ARIMA, Pandas, Excel",
        "what": "Developed and validated multiple forecasting models, implemented ensemble approach, and packaged outputs into monthly Excel reports with scenario planning.",
        "impact": "Improved forecast accuracy by ~18% vs prior approach and enabled scenario-driven promotional budgeting.",
        "impact_pct": 18,
        "tags": ["Forecasting","Time Series"],
        "repo": "#",
        "sample_data": [
            {"date":"2023-01-01","sales":1200},{"date":"2023-02-01","sales":1350},{"date":"2023-03-01","sales":1280}
        ]
    },
    {
        "title": "Portfolio Risk Heatmap",
        "problem": "Risk managers lacked a consolidated view of exposures across business units.",
        "data": "Internal exposure tables, transaction logs, external risk scores",
        "tools": "Python, GeoPlot/Plotly, SQL",
        "what": "Created a heatmap-driven interface highlighting high-risk clusters and root-cause drill-downs; implemented automated alerts for threshold breaches.",
        "impact": "Allowed prioritization of remediation efforts; reduced high-risk exposure by 12% within two quarters.",
        "impact_pct": 12,
        "tags": ["Risk","Geo"],
        "repo": "#",
        "sample_data": [
            {"region":"North","risk_score":78},{"region":"South","risk_score":54},{"region":"East","risk_score":89}
        ]
    }
]

for proj in featured:
    # Interactive expander per project
    with st.expander(proj['title']):
        left, right = st.columns([3, 1])
        with left:
            st.markdown(f"**Problem:** {proj['problem']}")
            st.markdown(f"**Data (source):** {proj['data']}")
            st.markdown(f"**Tools used:** {proj['tools']}")
            st.markdown(f"**What I did:** {proj['what']}")
            st.markdown(f"**Impact:** {proj['impact']}")

            # buttons to show sample data or open repo
            col_a, col_b = st.columns([1,1])
            if col_a.button("Show sample data", key=f"data_{proj['title']}"):
                df = pd.DataFrame(proj.get('sample_data', []))
                st.dataframe(df)
            if col_b.button("View repo", key=f"repo_{proj['title']}"):
                st.markdown(f"[Open repository]({proj.get('repo','#')})")

            # small demo chart if time-series or numeric
            if st.button("Show demo chart", key=f"chart_{proj['title']}"):
                df = pd.DataFrame(proj.get('sample_data', []))
                if 'sales' in df.columns or 'Market_Share' in df.columns or 'risk_score' in df.columns:
                    if 'date' in df.columns:
                        df['date'] = pd.to_datetime(df['date'])
                        fig = px.line(df, x='date', y=[c for c in df.columns if c!='date'])
                    elif 'Market_Share' in df.columns:
                        fig = px.bar(df, x='Brand', y='Market_Share')
                    elif 'risk_score' in df.columns:
                        fig = px.bar(df, x='region', y='risk_score')
                    else:
                        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
                    st.plotly_chart(fig, use_container_width=True)

        with right:
            if proj.get('impact_pct'):
                st.metric("Impact (%)", f"{proj['impact_pct']}%")
                st.progress(min(proj['impact_pct'] / 100.0, 1.0))
            else:
                st.write(proj.get('impact', ''))

st.markdown('</div>', unsafe_allow_html=True)

try:
    from components.footer import render_footer
    render_footer()
except Exception:
    pass
