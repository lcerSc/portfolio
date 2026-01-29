import streamlit as st


def render_footer(email: str = "shaedimran12@gmail.com", phone: str = "+254789631344", hours: str = "Mon–Fri 9:00–17:00", slogan: str = "Turning data into decisions.", linkedin: str = "https://www.linkedin.com", github: str = "https://github.com"):
    # Simple SVG icons inline for LinkedIn and GitHub
    linkedin_svg = """
    <svg class='footer-icon' width='16' height='16' viewBox='0 0 24 24' fill='currentColor' xmlns='http://www.w3.org/2000/svg'>
      <path d='M4.98 3.5C4.98 4.88 3.86 6 2.48 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM0 8h5v16H0V8zM8 8h4.8v2.2h.1c.7-1.3 2.4-2.7 4.9-2.7 5.2 0 6.2 3.4 6.2 7.8V24h-5V16.1c0-1.9 0-4.4-2.7-4.4-2.7 0-3.1 2.1-3.1 4.3V24H8V8z'/>
    </svg>
    """
    github_svg = """
    <svg class='footer-icon' width='16' height='16' viewBox='0 0 24 24' fill='currentColor' xmlns='http://www.w3.org/2000/svg'>
      <path d='M12 .5C5.7.5.6 5.6.6 11.9c0 5.1 3.3 9.5 7.9 11.1.6.1.8-.3.8-.6v-2.1c-3.2.7-3.9-1.4-3.9-1.4-.5-1.2-1.2-1.5-1.2-1.5-1-.7.1-.7.1-.7 1.1.1 1.7 1.2 1.7 1.2 1 .1 1.6.8 1.9 1.2 1.1-.1 2.2-.5 3.1-1-.3-.8-.9-1.5-1.6-1.8-2.6-.3-5.3-1.3-5.3-5.8 0-1.3.4-2.4 1.2-3.2-.1-.3-.5-1.7.1-3.5 0 0 1-.3 3.3 1.2.9-.3 1.9-.5 2.9-.5s2.1.2 2.9.5c2.3-1.5 3.3-1.2 3.3-1.2.6 1.8.2 3.2.1 3.5.8.8 1.2 1.9 1.2 3.2 0 4.5-2.7 5.5-5.3 5.8.6.5 1 1.3 1 2.6v3.9c0 .3.2.7.8.6 4.6-1.6 7.9-6 7.9-11.1C23.4 5.6 18.3.5 12 .5z'/>
    </svg>
    """

    html = f"""
    <div class="site-footer">
      <div class="footer-inner">
        <div class="footer-left">
          <strong>Contact</strong>: <a href="mailto:{email}">{email}</a> • <a href="tel:{phone}">{phone}</a>
        </div>
        <div class="footer-center">Hours: {hours}</div>
        <div class="footer-right">{slogan} &nbsp; <a href="{linkedin}" target="_blank" rel="noreferrer">{linkedin_svg}</a> <a href="{github}" target="_blank" rel="noreferrer">{github_svg}</a></div>
      </div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
