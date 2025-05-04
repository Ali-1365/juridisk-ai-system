from fastapi import FastAPI
from pydantic import BaseModel
from modules import (
    nlu_parser, argumentation_engine, risk_assessor,
    precedent_matcher, strategy_recommender, damage_calculator
)

app = FastAPI(title="Juridisk AI-API", version="1.0")

class TextRequest(BaseModel):
    pass
    text: str

class DamageRequest(BaseModel):
    income_loss: int
    months: int
    sveda_vark: int = 20000
    ideell_skada: int = 10000

@app.post("/analyze-text")
def analyze_text(req: TextRequest):
    risks = risk_assessor.assess_risks(req.text)
    precedents = precedent_matcher.match_precedent(req.text)
    return {
        "nlu": nlu_parser.parse_document(req.text),
        "argumentation": argumentation_engine.analyze_arguments(req.text),
        "risks": risks,
        "precedents": precedents,
        "strategy": strategy_recommender.recommend_strategy(risks, precedents)
    }

@app.post("/calculate-damages")
def calculate_damages(req: DamageRequest):
    return damage_calculator.calculate_damages(
        req.income_loss, req.months, req.sveda_vark, req.ideell_skada
    )
