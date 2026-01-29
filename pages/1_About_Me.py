import streamlit as st

# page wrapper to apply theme styles
st.markdown('<div class="theme-card">', unsafe_allow_html=True)

st.markdown("<h2 class='page-title'>👤 About Me</h2>", unsafe_allow_html=True)
st.markdown('<div class="section-underline"></div>', unsafe_allow_html=True)

st.write(
    """
    I am a **Data Analyst** with a background in **Actuarial Science**, 
    specializing in data-driven insights, market analysis, and financial analytics.
    
    I have hands-on experience using Python, Excel, and analytical tools 
    to transform raw data into actionable business intelligence.
    """
)

st.subheader("🎓 Education & Certifications")
st.markdown(
    """
    - Degree in Actuarial Science  
    - Cisco – Data Analytics Essentials  
    - AFRICDSA – Advanced Excel  
    - Macabacus – Financial Modeling & Financial Statements  
    - Hashgraph Developer Association  
    """
)

st.subheader("🛠 Technical Skills")
st.markdown(
    """
    - Python (Pandas, NumPy, Streamlit, Plotly)
    - Advanced Microsoft Excel
    - Data Cleaning & Analysis
    - Market & Competitor Analysis
    - Financial Reporting & Ethics
    """
)

# skill chips for visual interest
st.markdown('<div class="skill-chips">', unsafe_allow_html=True)
skills = ["Python", "Pandas", "Plotly", "Excel", "Power BI", "SQL", "Financial Modeling"]
for s in skills:
    st.markdown(f'<div class="skill-chip">{s}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Download CV and social links
st.markdown('<div style="margin-top:10px">', unsafe_allow_html=True)
st.markdown('<a class="download-cta" href="#" target="_blank">Download CV</a> <span style="margin-left:8px"></span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.subheader("🎯 Career Focus")
st.write(
    """
    I am interested in roles where data supports **strategy, market intelligence, 
    and business decision-making**, particularly in consulting and technology-driven environments.
    """
)

# close themed wrapper
st.markdown('</div>', unsafe_allow_html=True)

# Startups section
st.markdown("<h3 style='margin-top:18px'>🚀 Startups I'm building</h3>", unsafe_allow_html=True)
st.markdown('<div class="section-underline" style="width:120px"></div>', unsafe_allow_html=True)
st.markdown('<div class="project-grid">', unsafe_allow_html=True)
startups = [
    {
        'name': 'Analytics Data Hub KE',
        'role': 'Founder / Data Lead',
        'desc': 'A platform to centralize, clean and serve analytics datasets for Kenyan SMEs and NGOs.',
        'status': 'Design & MVP',
        'focus': 'Data pipelines, analytics-as-a-service'
    },
    {
        'name': 'NexGen Investments',
        'role': 'Co-founder / Strategy',
        'desc': 'Early-stage investment vehicle focused on tech-enabled businesses in East Africa.',
        'status': 'Concept & Partnerships',
        'focus': 'Deal sourcing, financial modelling'
    }
]
for s in startups:
    html = f"""
    <div class='project-card'>
            <h4><a class='project-cta' href='/?page=pages/startup_{s['name'].lower().replace(' ', '_')}.py'>{s['name']}</a></h4>
      <p><strong>Role:</strong> {s['role']}</p>
      <p><strong>Focus:</strong> {s['focus']}</p>
      <p>{s['desc']}</p>
      <p><strong>Status:</strong> {s['status']}</p>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

try:
    from components.footer import render_footer
    render_footer()
except Exception:
    pass
