import streamlit as st
from modules import (
    nlu_parser,
    argumentation_engine,
    risk_assessor,
    precedent_matcher,
    strategy_recommender,
    damage_calculator
)

st.set_page_config(page_title="Juridisk AI-analys", layout="wide")

st.title("AI-baserad juridisk analys för advokater")
st.markdown("Ladda upp ett juridiskt dokument eller klistra in text för att få analys, riskbedömning och strategiförslag.")

text_input = st.text_area("Klistra in juridisk text här:", height=300)

if st.button("Analysera"):
    if not text_input.strip():
        st.warning("Text saknas.")
    else:
        st.subheader("1. Dokumentanalys (NLU)")
        nlu = nlu_parser.parse_document(text_input)
        st.json(nlu)

        st.subheader("2. Argumentationsanalys")
        st.write(argumentation_engine.analyze_arguments(text_input))

        st.subheader("3. Riskbedömning")
        risks = risk_assessor.assess_risks(text_input)
        st.write(risks)

        st.subheader("4. Prejudikatmatchning")
        precedents = precedent_matcher.match_precedent(text_input)
        st.write(precedents)

        st.subheader("5. Strategiförslag")
        strategies = strategy_recommender.recommend_strategy(risks, precedents)
        st.write(strategies)

st.sidebar.header("Skadeståndsberäkning")
loss = st.sidebar.number_input("Inkomstbortfall per månad", 0, 100000, 20000)
months = st.sidebar.number_input("Antal månader", 0, 36, 6)
sveda = st.sidebar.number_input("Sveda och värk", 0, 100000, 20000)
ideell = st.sidebar.number_input("Ideell skada", 0, 100000, 10000)

if st.sidebar.button("Beräkna skadestånd"):
    result = damage_calculator.calculate_damages(loss, months, sveda, ideell)
    st.sidebar.subheader("Resultat")
    st.sidebar.json(result)
