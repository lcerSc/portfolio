# Streamlit Portfolio

This repository contains a Streamlit-based portfolio site with a blue/white/black theme, interactive project demos, and multiple pages.

Run locally:

```powershell
venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py
```
Automated deploy to Streamlit Community Cloud

This repo includes a GitHub Action that triggers a deploy on push to `main`. To enable it:

1. Create an app on Streamlit Community Cloud (https://share.streamlit.io) and note the **App ID**.
2. Create a Streamlit API token (from your Streamlit account settings) and copy the token.
3. In this GitHub repo, add two repository secrets: `STREAMLIT_API_TOKEN` and `STREAMLIT_APP_ID`.
4. Push to `main` — the `streamlit-deploy` workflow will POST to Streamlit's Deployments API to trigger a new deployment.

Note: Streamlit Community Cloud usually supports direct GitHub connection which can also auto-deploy; this workflow offers an alternative programmatic trigger.
