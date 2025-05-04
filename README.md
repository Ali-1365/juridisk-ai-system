# Juridisk AI-analys (Streamlit-version)

Detta är en fullständig juridisk AI-applikation för advokater, baserad på svensk rätt. Projektet innehåller:

## Funktionalitet
- Naturlig språkförståelse (NLU)
- Formaliabedömning (ex. FL 25 §, partsbrister)
- Argumentationsanalys
- Riskidentifiering och strategi
- Matchning av HFD/HD-praxis
- Skadeståndsberäkning
- Webbaserat gränssnitt (Streamlit)

## 


```bash
pip install -r requirements.txt
streamlit run app.py
```

## Exempelfil

`testcases/test_input.txt` innehåller ett verkligt ärende som kan analyseras direkt.

## Teknisk struktur

- `modules/` – AI-komponenter
- `testcases/` – testfall
- `app.py` – Streamlit-gränssnitt
- `requirements.txt` – beroenden
