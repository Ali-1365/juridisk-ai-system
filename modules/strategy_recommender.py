"""
Föreslår juridiska strategier beroende på ärendeinnehåll och risker
"""

def recommend_strategy(risks, precedents):
    strategy = []

    if any("FL 25 §" in r for r in risks):
        strategy.append("Yrkande om ogiltigförklaring pga kommunikationsbrist")
    if any("HFD 2021 ref. 63" in p for p in precedents):
        strategy.append("Åberopa rättshandlingskonversion och begär ny prövning")
    if not strategy:
        strategy.append("Komplettera ärendet med medicinsk bevisning och begär inhibition")

    return strategy
