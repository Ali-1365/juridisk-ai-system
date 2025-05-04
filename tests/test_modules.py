import pytest
from modules import (
    nlu_parser,
    argumentation_engine,
    risk_assessor,
    precedent_matcher,
    strategy_recommender,
    damage_calculator
)

test_text = (
    "Överklagande av Försäkringskassans beslut. Beslutet fattades utan kommunikation "
    "enligt FL 25 §. SGI sattes till 0. HFD 2021 ref. 63 är relevant."
)

def test_nlu_parser():
    result = nlu_parser.parse_document(test_text)
    assert "Försäkringskassan" in result["myndighet"]
    assert "SGI" in result["identifierade_begrepp"]

def test_argumentation_engine():
    result = argumentation_engine.analyze_arguments(test_text)
    assert "Formaliabrist" in result

def test_risk_assessor():
    risks = risk_assessor.assess_risks(test_text)
    assert any("Formaliafel" in r for r in risks)

def test_precedent_matcher():
    matches = precedent_matcher.match_precedent(test_text)
    assert "HFD 2021 ref. 63" in matches

def test_strategy_recommender():
    risks = risk_assessor.assess_risks(test_text)
    precedents = precedent_matcher.match_precedent(test_text)
    strategy = strategy_recommender.recommend_strategy(risks, precedents)
    assert isinstance(strategy, list)
    assert len(strategy) > 0

def test_damage_calculator():
    result = damage_calculator.calculate_damages(20000, 6, 20000, 10000)
    assert result["totalbelopp"] == 20000*6 + 20000 + 10000
