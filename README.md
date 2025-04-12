# social-pulse-ai 
 
Geo-aware social media sentiment analysis platform 
 
## Features 
- Real-time social media ingestion (Twitter/X, Reddit) 
- AI-powered sentiment analysis 
- Geographic visualization 
 🚀 **What's Next**  
 
_This project is under active development! Coming soon:_  
- [ ] Reddit integration (ETA: MM/DD)  
- [ ] Multi-language support  
- [ ] AWS Lambda scaling 
## Quick Start 
```bash 
# Setup 
python -m venv venv 
venv\Scripts\activate 
pip install -r requirements.txt 
 
# Run API 
uvicorn backend.api.main:app --reload 
 
# Run Dashboard 
streamlit run dashboard/streamlit_app/main.py 
``` 
