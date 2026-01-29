import streamlit as st

st.set_page_config(
    page_title="Imran | Data Analyst Portfolio",
    page_icon="📊",
    layout="wide"
)


def _local_css(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        # If CSS is missing, don't break the app — continue without styles.
        pass


# load theme styles
_local_css("static/styles.css")

# ---- HEADER ----
st.markdown(
                """
                <div class="hero fade-in">
                    <div class="hero-grid">
                        <div class="hero-content">
                            <h1 style='text-align: left; margin-bottom:6px;'>📊 Imran</h1>
                            <p style='text-align: left; margin:0; color: rgba(234,244,255,0.95);'>
                                Data Analyst • Market Intelligence • Actuarial Science • Business Analytics
                            </p>
                            <div class="hero-actions">
                                <a class="cta-button" href="#" target="_blank">Download CV</a>
                                <a class="social-link" href="mailto:shaedimran12@gmail.com">
                                    <svg class="social-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5L4 8V6l8 5 8-5v2z"/></svg>
                                    <span style="margin-left:6px">Email</span>
                                </a>
                                <a class="social-link" href="https://www.linkedin.com" target="_blank">
                                    <svg class="social-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M4.98 3.5C4.98 4.88 3.86 6 2.48 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM0 8h5v16H0V8zM8 8h4.8v2.2h.1c.7-1.3 2.4-2.7 4.9-2.7 5.2 0 6.2 3.4 6.2 7.8V24h-5V16.1c0-1.9 0-4.4-2.7-4.4-2.7 0-3.1 2.1-3.1 4.3V24H8V8z"/></svg>
                                    <span style="margin-left:6px">LinkedIn</span>
                                </a>
                                <a class="social-link" href="https://github.com" target="_blank">
                                    <svg class="social-icon" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 .5C5.7.5.6 5.6.6 11.9c0 5.1 3.3 9.5 7.9 11.1.6.1.8-.3.8-.6v-2.1c-3.2.7-3.9-1.4-3.9-1.4-.5-1.2-1.2-1.5-1.2-1.5-1-.7.1-.7.1-.7 1.1.1 1.7 1.2 1.7 1.2 1 .1 1.6.8 1.9 1.2 1.1-.1 2.2-.5 3.1-1-.3-.8-.9-1.5-1.6-1.8-2.6-.3-5.3-1.3-5.3-5.8 0-1.3.4-2.4 1.2-3.2-.1-.3-.5-1.7.1-3.5 0 0 1-.3 3.3 1.2.9-.3 1.9-.5 2.9-.5s2.1.2 2.9.5c2.3-1.5 3.3-1.2 3.3-1.2.6 1.8.2 3.2.1 3.5.8.8 1.2 1.9 1.2 3.2 0 4.5-2.7 5.5-5.3 5.8.6.5 1 1.3 1 2.6v3.9c0 .3.2.7.8.6 4.6-1.6 7.9-6 7.9-11.1C23.4 5.6 18.3.5 12 .5z"/></svg>
                                    <span style="margin-left:6px">GitHub</span>
                                </a>
                            </div>
                        </div>
                        <div class="hero-avatar">
                            <img class="avatar-img" src="https://ui-avatars.com/api/?name=Imran&background=0b63ff&color=fff&size=256" alt="Imran" />
                        </div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
)

# subtle divider
st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

# ---- INTRO ----
st.write(
    """
    Welcome to my data analytics portfolio.  
    This platform showcases Projects tackled, real-world analytics, market insights, 
    and data-driven decision-making using Python, Microsoft Excel, and Power BI(Visualization). My ability to transform raw data into meaningful insights that support business, market and strategic decision-making. The work present here on my portfolio pages refelcts strong foundation in data analytics, market intelligence, and quantitative analysis backed by actuarial science. Through this portfolio, i highlight practical applications of data analysis using python, microsoft excel and modern visualization tools to explore trends, evaluate performance, and uncover actionable insights. the projects focus on real world scenarios such as market analysis, competitor benchmarking, performance tracking, and data driven reporting. My approach emphasizes on clarity, accuracy, and ethical data handling ensuring that insights are not only technically sound but also relevant and easy for stakeholders to understand. this portfolio is designed to reflect how i think as an analyst-structured, analytica, focused on delivering value through data.
    """
)

# quick stats and CTA
st.markdown(
        """
        <div class="stats-row">
            <div class="stat">
                <div class="stat-number">12+</div>
                <div class="stat-label">Projects delivered</div>
            </div>
            <div class="stat">
                <div class="stat-number">3 yrs</div>
                <div class="stat-label">Analytical experience</div>
            </div>
            <div class="stat">
                <div class="stat-number">95%</div>
                <div class="stat-label">Client satisfaction</div>
            </div>
        </div>
        <div style="margin-top:12px;">&nbsp;</div>
        """,
        unsafe_allow_html=True
)

# Use a Streamlit button to navigate to the Projects page reliably
if st.button("Explore Projects", key="explore_projects"):
    try:
        # Use a small client-side redirect to ensure the app navigates to the Projects page
        st.components.v1.html("<script>window.location.href='/?page=pages/3_Projects.py';</script>", height=0)
    except Exception:
        st.markdown("[Open Projects](/?page=pages/3_Projects.py)")

# ---- SIDEBAR ----
with st.sidebar:
    st.title("Navigation")
    st.page_link("app.py", label="Home")
    st.page_link("pages/1_About_Me.py", label="About Me")
    st.page_link("pages/2_Market_Analysis.py", label="Market Analysis")
    st.page_link("pages/3_Projects.py", label="Projects done")
  

# render global footer (safe import)
try:
    from components.footer import render_footer
    render_footer()
except Exception:
    pass


