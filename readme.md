# Ultimate NSE Cockpit Deployment


## 1. Install dependencies
pip install -r requirements.txt


## 2. Run locally
streamlit run main_app.py


## 3. Deploy on Streamlit Cloud
1. Push repository to GitHub.
2. Create a new app on Streamlit Cloud.
3. Connect your GitHub repo.
4. Ensure `main_app.py` is the main module.
5. Make sure `requirements.txt` is included.
6. Deploy.


## 4. Telegram alerts
- Edit `config.py` with your bot token and chat ID.