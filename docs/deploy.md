# Installation & Deployment

## Lokalt
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Docker
```bash
docker build -t juridisk-ai .
docker run -p 8501:8501 juridisk-ai
```

## API
```bash
pip install -r requirements-api.txt
uvicorn api:app --reload
```
